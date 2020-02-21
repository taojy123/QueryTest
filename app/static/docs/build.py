from eave import *

doc = Doc(
    title='接口文档',
    version='1.0.0',
    host='http://taojy123.com:8000',
    description='',
)

doc.add_api(
    title='新产品试用申请',
    description='',
    uri='/api/trail/',
    method='POST',
    body_params=[
        BP(name='product_name', description='产品名称', required=True),
        BP(name='name', description='用户姓名', required=True),
        BP(name='mobile', description='联系手机', required=True),
        BP(name='company_name', description='单位名称', required=True),
        BP(name='company_domain', description='单位领域', required=True),
        BP(name='company_city', description='单位省市', required=True),
        BP(name='company_address', description='详细地址', required=True),
        BP(name='company_email', description='单位邮箱', required=True),
        BP(name='detail', description='需求描述', required=True),
    ],
    content_types=['application/json'],
    body_example="""
{
    "product_name": "xxx产品名称",
    "name": "xxx用户姓名",
    "mobile": "xxx联系手机",
    "company_name": "xxx单位名称",
    "company_domain": "xxx单位领域",
    "company_city": "xxx单位省市",
    "company_address": "xxx详细地址",
    "company_email": "xxx单位邮箱",
    "detail": "xxx需求描述"
}
""",
)

doc.add_api(
    title='日志统计',
    description='',
    uri='/api/query_statistics/',
    method='GET',
    query_params=[
        QP(name='year', description='按年统计', required=True, example='2020'),
        QP(name='month', description='按月统计', required=False, example='02'),
        QP(name='day', description='按日统计', required=False, example='24'),
        QP(name='product_name', description='产品名称', required=False, example='沃信分'),
        QP(name='result', description='查询状态', required=False, example='未查得'),
        QP(name='period', description='响应时间', required=False, example='1-3秒内'),
    ],
    response_example="""
[{
    "time_code": "20190403",
    "product_name": "个人资质等级",
    "result": "未查得",
    "period": "1秒以内",
    "count": 1,
    "price_rule": "查询计费",
    "unit_price": 12,
    "price": 12,
    "product_code": "002",
    "remark": null
}, {
    "time_code": "20190403",
    "product_name": "个人资质等级",
    "result": "超时",
    "period": "6-10秒内",
    "count": 8,
    "price_rule": "查得计费",
    "unit_price": 13,
    "price": 104,
    "product_code": "002",
    "remark": null
}]
""",
    tips='参考 http://taojy123.com:8000/',
)


doc.add_api(
    title='年度趋势',
    description='展示一年中每个月的调用次数',
    uri='/api/year_statistics/',
    method='GET',
    query_params=[
        QP(name='year', description='年份', required=True, example='2020'),
        QP(name='product_name', description='产品名称', required=False, example='沃信分'),
        QP(name='result', description='查询状态', required=False, example='未查得'),
        QP(name='period', description='响应时间', required=False, example='1-3秒内'),
    ],
    response_example="""
[{
        "time_code": "202001",
        "count": 246
    },
    {
        "time_code": "202002",
        "count": 161
    },
    {
        "time_code": "202003",
        "count": 0
    },
    {
        "time_code": "202004",
        "count": 0
    }
]
""",
)


doc.add_api(
    title='月度趋势',
    description='展示一个月中每天的调用次数',
    uri='/api/month_statistics/',
    method='GET',
    query_params=[
        QP(name='year', description='年份', required=True, example='2020'),
        QP(name='month', description='月份（如果不传则为上一个月）', required=False, example='02'),
        QP(name='product_name', description='产品名称', required=False, example='沃信分'),
        QP(name='result', description='查询状态', required=False, example='未查得'),
        QP(name='period', description='响应时间', required=False, example='1-3秒内'),
    ],
    response_example="""
[{
        "time_code": "20200101",
        "count": 87
    },
    {
        "time_code": "20200102",
        "count": 78
    },
    {
        "time_code": "20200103",
        "count": 76
    }
]
""",
)


doc.add_api(
    title='每日趋势',
    description='展示一段时间内每天的调用次数',
    uri='/api/day_statistics/',
    method='GET',
    query_params=[
        QP(name='start', description='起始日期', required=True, example='2020-01-29'),
        QP(name='end', description='终止日期', required=True, example='2020-02-01'),
        QP(name='product_name', description='产品名称', required=False, example='沃信分'),
        QP(name='result', description='查询状态', required=False, example='查得'),
    ],
    response_example="""
[{
        "time_code": "20200129",
        "count": 77
    },
    {
        "time_code": "20200130",
        "count": 80
    },
    {
        "time_code": "20200131",
        "count": 46
    },
    {
        "time_code": "20200201",
        "count": 50
    }
]
""",
)


doc.add_api(
    title='日志详情',
    description='',
    uri='/api/query_detail/',
    method='GET',
    query_params=[
        QP(name='start', description='起始日期', required=True, example='2020-01-24'),
        QP(name='end', description='终止日期', required=True, example='2020-01-28'),
        QP(name='product_name', description='产品名称', required=False, example='沃信分'),
        QP(name='result', description='查询状态', required=False, example='查得'),
    ],
    response_example="""
[{
    "time_code": "20200212",
    "product_name": "沃信分",
    "result": "出错",
    "time": "2020-02-12 05:11:51",
    "query_id": "0325978c70f04bdf94f64cc48d7111c5",
    "price_rule": "查询计费",
    "unit_price": 17,
    "request": "{}",
    "response": "{}",
    "status_code": "200",
    "return_time": "6",
    "period": "9",
    "product_code": "002",
    "remark": null
}, {
    "time_code": "20200212",
    "product_name": "沃信分",
    "result": "查得",
    "time": "2020-02-12 05:11:51",
    "query_id": "09d7574a5aba418cad1c239abb95e6ab",
    "price_rule": "字段计费",
    "unit_price": 8,
    "request": "{}",
    "response": "{}",
    "status_code": "200",
    "return_time": "8",
    "period": "3",
    "product_code": "001",
    "remark": null
}]
""",
    tips='参考 http://taojy123.com:8000/detail/',
)


doc.add_api(
    title='日最高访问量',
    description='',
    uri='/api/best_day/',
    method='GET',
    query_params=[
        QP(name='product_name', description='产品名称', required=True, example='product_name'),
    ],
    response_example="""
{
    "value": 3000,
    "time": "20200124"
}
""",
)


doc.add_api(
    title='月最高访问量',
    description='',
    uri='/api/best_month/',
    method='GET',
    query_params=[
        QP(name='product_name', description='产品名称', required=True, example='product_name'),
    ],
    response_example="""
{
    "value": 30000,
    "time": "202002"
}
""",
)


doc.add_api(
    title='当年累计访问量',
    description='',
    uri='/api/total_year/',
    method='GET',
    query_params=[
        QP(name='product_name', description='产品名称', required=True, example='product_name'),
    ],
    response_example="""
{
    "value": 90000,
    "time": "2020"
}
""",
)


doc.build('doc.html', 'zh')
