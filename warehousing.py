import datetime
import json
import os

from kafka import KafkaConsumer

from app.cassandra_models import QueryStatistics, QueryDetail


# export CASS_HOSTS=172.23.43.16,172.23.43.21,172.23.43.22
# export KAFKA_HOST=172.23.43.21:9092
# python warehousing.py


KAFKA_HOST = os.getenv('KAFKA_HOST', '172.23.43.21:9092')

consumer = KafkaConsumer('querymessages', bootstrap_servers=KAFKA_HOST, group_id='warehousing-querymessages')


def statistics_count(detail, time_code):
    
    period_s = detail.period / 1000
    if period_s < 1:
        period = '1秒以内'
    elif period_s < 3:
        period = '1-3秒内'
    elif period_s < 6:
        period = '3-6秒内'
    elif period_s < 10:
        period = '6-10秒内'
    elif period_s < 15:
        period = '10-15秒内'
    else:
        period = '15秒以上'
    
    rs = QueryStatistics.filter(time_code=time_code, product_name=detail.product_name, result=detail.result, period=period).limit(1)
    if rs:
        r = rs[0]
    else:
        r = QueryStatistics.create(time_code=time_code, product_name=detail.product_name, result=detail.result, period=period)
    r.count += 1
    r.price_rule = detail.price_rule
    r.unit_price = detail.unit_price
    r.price = detail.unit_price * r.count
    r.product_code = detail.product_code
    r.save()


for msg in consumer:
    print(msg.topic, msg.offset)
    value = json.loads(msg.value)
    message = json.loads(value['message'])
    
    started_at = message['started_at']  # ms
    finished_at = message['finished_at']  # ms
    started_time = datetime.datetime.fromtimestamp(started_at / 1000)
    finished_time = datetime.datetime.fromtimestamp(finished_at / 1000)

    query_id = message['kong_request_id']
    time_code = started_time.strftime('%Y%m%d')
    product_name = message['service']['name']
    result = '查询'
    time = started_time.strftime('%Y-%m-%d %H:%M:%S')
    price_rule = '-'
    unit_price = 0
    request = json.dumps(message['request'])
    response = json.dumps(message['response'])
    status_code = str(message['response']['status'])
    return_time = finished_time.strftime('%Y-%m-%d %H:%M:%S')
    period = finished_at - started_at  # ms
    product_code = message['service']['name']
    
    if int(status_code) >= 400:
        result = '出错'

    detail = QueryDetail.create(
        query_id=query_id,
        time_code=time_code,
        product_name=product_name,
        result=result,
        time=time,
        price_rule=price_rule,
        unit_price=unit_price,
        request=request,
        response=response,
        status_code=status_code,
        return_time=return_time,
        period=period,
        product_code=product_code,
    )

    year_code = time_code[:4]
    month_code = time_code[:6]
    day_code = time_code
    
    statistics_count(detail, year_code)
    statistics_count(detail, month_code)
    statistics_count(detail, day_code)


message = {
    'finished_at': 1583724966501,
     'consumer': {'custom_id': 'inner', 'created_at': 1562062690, 'id': '42bed3e5-2244-4f42-bdc9-0961143e3153',
                  'username': 'hjp'}, 'latencies': {'request': 11, 'kong': 2, 'proxy': 8},
     'service': {'host': 'demo.test', 'created_at': 1574128859, 'connect_timeout': 60000,
                 'id': '50cdcb12-d837-438a-b0d9-3f56aa2e2baa', 'protocol': 'http', 'name': 'demo',
                 'read_timeout': 60000, 'port': 8000, 'path': '/api/demo/v1', 'updated_at': 1574128859, 'retries': 5,
                 'write_timeout': 60000},
     'tries': [{'balancer_latency': 0, 'port': 8000, 'balancer_start': 1583724966492, 'ip': '10.42.2.181'}],
     'data_source': 'cache', 'upstream_uri': '/api/demo/v1',
     'request': {'querystring': {}, 'size': '627', 'uri': '/api/demo/v1', 'tls': '',
                 'url': 'http://taiqiyun.wowfintech.cn/api/demo/v1',
                 'headers': {'host': 'taiqiyun.wowfintech.cn', 'content-type': 'application/json',
                             'x-real-ip': '172.23.43.15', 'x-forwarded-port': '80', 'x-original-uri': '/api/demo/v1',
                             'x-credential-username': 'hmacuser',
                             'kong-request-id': '9c106bb4-6e6d-4e69-81f4-905a0b3d9377#292',
                             'x-request-id': '29b8212634f4fffdd85c572e29f802dd', 'x-consumer-username': 'hjp',
                             'x-consumer-custom-id': 'inner', 'x-forwarded-host': 'taiqiyun.wowfintech.cn',
                             'accept': '*/*', 'x-consumer-id': '42bed3e5-2244-4f42-bdc9-0961143e3153',
                             'username': 'hmacuser',
                             'authorization': 'hmac username="hmacuser", algorithm="hmac-sha256",headers="x-date username", signature="XjBB5ghK4nncD7fdhX1Tz3hV/h9w8RpmnBevQFRR9lo="',
                             'x-forwarded-proto': 'http', 'content-length': '16', 'x-forwarded-for': '172.23.43.15',
                             'user-agent': 'python-requests/2.22.0',
                             'signature': 'XjBB5ghK4nncD7fdhX1Tz3hV/h9w8RpmnBevQFRR9lo=',
                             'x-date': 'Mon, 09 Mar 2020 03:36:06 GMT', 'accept-encoding': 'gzip, deflate',
                             'x-scheme': 'http'}, 'body': '{"name":"cloud"}', 'method': 'POST'},
     'client_ip': '172.23.43.15', 'real_ip': '172.23.43.15',
     'authenticated_entity': {'id': '447a7a9d-6d73-4f03-bc36-497197c06cc9'},
     'kong_request_id': '9c106bb4-6e6d-4e69-81f4-905a0b3d9377#292',
     'response': {'body': '{"data":{"code":0,"data":{"is_match":1},"msg":"\\u6210\\u529f","timeout":60}}\n',
                  'headers': {'content-type': 'application/json', 'date': 'Mon, 09 Mar 2020 03:36:06 GMT',
                              'server': 'gunicorn/19.9.0', 'connection': 'close', 'transfer-encoding': 'chunked',
                              'kong-request-id': '9c106bb4-6e6d-4e69-81f4-905a0b3d9377#292'}, 'status': 200,
                  'size': '374'},
     'route': {'strip_path': True, 'updated_at': 1574128860, 'protocols': ['http', 'https'], 'name': 'demo',
               'preserve_host': True, 'regex_priority': 0, 'created_at': 1574128860, 'paths': ['/api/demo/v1'],
               'https_redirect_status_code': 426, 'service': {'id': '50cdcb12-d837-438a-b0d9-3f56aa2e2baa'},
               'id': '00dd0e10-c7a1-4a4c-a972-7b47ef63be96'},
    'started_at': 1583724966490}
