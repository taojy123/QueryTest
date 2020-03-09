# Python3.6+
# pip install cassandra-driver

import datetime
import os
import random
import uuid

from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model


class QueryStatistics(Model):
    """
    请求统计日志，以时间、产品、查询结果、响应时间 4个维度来统计
    例如：20200124这一天，沃信分产品，查得 的请求数量为 5000
    又如：202001这个月，沃信分产品，未查得，响应时间在1-3秒内的请求数量为 8000
    """

    __table_name__ = 'query_statistics'

    time_code = columns.Text(primary_key=True)  # 统计时间 2020 / 202001 / 20200124
    product_name = columns.Text(primary_key=True)  # 产品名称
    result = columns.Text(primary_key=True)  # 查询结果: 查得、未查得、出错、超时
    period = columns.Text(primary_key=True)  # 响应时间: '1秒以内', '1-3秒内', '3-6秒内', '6-10秒内', '10-15秒内', '15秒以上'
    count = columns.VarInt(default=0)  # 调用次数
    price_rule = columns.Text(required=False)  # 计价方式: 查得计费、字段计费、查询计费（由产品决定）
    unit_price = columns.VarInt(default=0)  # 单价
    price = columns.VarInt(default=0)  # 总价
    product_code = columns.Text(required=False)  # 产品编码
    remark = columns.Text(required=False)  # 备注
    created_at = columns.DateTime(default=datetime.datetime.now)  # 生成时间


class QueryDetail(Model):
    """
    请求详情日志，每一次对钛旗云 API 对调用生成一条记录
    以 query_id 为主键
    """

    __table_name__ = 'query_detail'

    query_id = columns.Text(primary_key=True)  # 请求序列号
    time_code = columns.Text(required=False)  # 统计日期 20200124
    product_name = columns.Text(required=False)  # 产品名称
    result = columns.Text(required=False)  # 查询结果: 查得、未查得、出错、超时
    time = columns.Text(required=False)  # 请求时间: 2020-02-21 10:20:40
    price_rule = columns.Text(required=False)  # 计价方式: 查得计费、字段计费、查询计费（由产品决定）
    unit_price = columns.VarInt(default=0)  # 单价
    request = columns.Text(required=False)  # 请求数据（脱敏后）
    response = columns.Text(required=False)  # 响应数据（脱敏后）
    status_code = columns.Text(required=False)  # 返回代码
    return_time = columns.Text(required=False)  # 返回时间
    period = columns.Text(required=False)  # 响应时间（毫秒）
    product_code = columns.Text(required=False)  # 产品编码
    remark = columns.Text(required=False)  # 备注
    created_at = columns.DateTime(default=datetime.datetime.now)  # 生成时间
        
    def save(self):
        instance = super().save()
        instance.save_redundant()
        return instance
    
    def save_redundant(self):
        """
        保存冗余数据
        """
        detail2 = QueryDetail2()
        for name, value in self.items():
            setattr(detail2, name, value)
        detail2.save()


class QueryDetail2(QueryDetail):
    """
    请求详情日志
    冗余
    多级主键，可以查询 20200124 这一天，沃信分产品，具体到每一个 API 请求的详情
    """

    __table_name__ = 'query_detail2'

    time_code = columns.Text(primary_key=True)
    product_name = columns.Text(primary_key=True)
    result = columns.Text(primary_key=True)
    time = columns.Text(primary_key=True)
    query_id = columns.Text(primary_key=True)


class Best(Model):
    """
    各产品的：
    日最高访问量
    月最高访问量
    当年累计访问量
    """

    __table_name__ = 'best'

    product_name = columns.Text(primary_key=True)  # 产品名称
    category = columns.Text(primary_key=True)  # 类别: 日最高访问量、月最高访问量、当年累计访问量
    value = columns.Text()  # 统计数值
    time = columns.Text(required=False)  # 统计时间点: 20200124、202002
    remark = columns.Text(required=False)  # 备注
    created_at = columns.DateTime(default=datetime.datetime.now)  # 生成时间


print('cassandra database init')

os.environ.setdefault('CQLENG_ALLOW_SCHEMA_MANAGEMENT', 'CQLENG_ALLOW_SCHEMA_MANAGEMENT')
keyspace = 'taiqiyun'

hosts = ['172.23.43.16', '172.23.43.21', '172.23.43.22']
# hosts = ['taojy123.com']

TI_HOST = os.getenv('TI_HOST')
if TI_HOST == 'taojy123.com':
    hosts = ['taojy123.com']

# export CASS_HOSTS=172.23.43.16,172.23.43.21,172.23.43.22
CASS_HOSTS = os.getenv('CASS_HOSTS')
if CASS_HOSTS:
    hosts = CASS_HOSTS.split(',')

connection.setup(hosts, keyspace, protocol_version=3)
sync_table(QueryStatistics)
sync_table(QueryDetail)
sync_table(QueryDetail2)
sync_table(Best)

print('database synced')


def fake_data():
    print('creating fake data')

    for i in range(400):

        now = datetime.datetime.now() - datetime.timedelta(i)

        for j in range(5):
            print('QueryStatistics', i)
            time_codes = [now.strftime('%Y%m%d')] * 30 + [now.strftime('%Y%m')] * 5 + [now.strftime('%Y')]
            time_code = random.choice(time_codes)
            product_name = random.choice(['个人资质等级', '沃信分'])
            result = random.choice(['查得', '未查得', '出错', '超时'])
            period = random.choice(['1秒以内', '1-3秒内', '3-6秒内', '6-10秒内', '10-15秒内', '15以上'])
            count = random.randint(1, 30)
            price_rule = random.choice(['查得计费', '字段计费', '查询计费'])
            unit_price = random.randint(5, 20)
            price = count * unit_price
            product_code = random.choice(['001', '002'])

            QueryStatistics.create(
                time_code=time_code,
                product_name=product_name,
                result=result,
                period=period,
                count=count,
                price_rule=price_rule,
                unit_price=unit_price,
                price=price,
                product_code=product_code,
            )

            for j in range(50):
                print('QueryDetail', j)

                time = now.strftime('%Y-%m-%d %H:%M:%S')
                query_id = uuid.uuid4().hex
                status_code = random.choice(['200', '200', '200', '200', '200', '400', '500'])
                return_time = str(random.randint(1, 10))
                period = str(random.randint(1, 10))

                QueryDetail.create(
                    time_code=time_code,
                    product_name=product_name,
                    result=result,
                    time=time,
                    query_id=query_id,
                    price_rule=price_rule,
                    unit_price=unit_price,
                    request='{}',
                    response='{}',
                    status_code=status_code,
                    return_time=return_time,
                    period=period,
                    product_code=product_code,
                )
    print('fake finish')


def fake_data2():
    product_names = ['个人资质等级', '沃信分']
    categories = ['日最高访问量', '月最高访问量', '当年累计访问量']
    for product_name in product_names:
        for category in categories:
            if category == '日最高访问量':
                time = '20200124'
            elif category == '月最高访问量':
                time = '202002'
            else:
                time = '2020'
            Best.create(
                product_name=product_name,
                category=category,
                value=str(random.randint(10000, 100000)),
                time=time,
            )

