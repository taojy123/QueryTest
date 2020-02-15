from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from app.cassandra_models import QueryStatistics, QueryDetail


def index(request):
    return render(request, 'index.html', locals())


def detail(request):
    return render(request, 'detail.html', locals())


def query_statistics_api(request):

    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')
    period = request.GET.get('period')

    time_code = ''
    if year:
        time_code = year
        if month:
            time_code += month
            if day:
                time_code += day
    print('time_code:', time_code)

    filter_args = {}

    if time_code:
        filter_args['time_code'] = time_code

        if product_name:
            filter_args['product_name'] = product_name

            if result:
                filter_args['result'] = result

                if period:
                    filter_args['period'] = period

    qs = QueryStatistics.objects.filter(**filter_args).limit(1000)

    rs = []
    for r in qs:
        rs.append({
            'time_code': r.time_code,
            'product_name': r.product_name,
            'result': r.result,
            'period': r.period,
            'count': r.count,
            'price_rule': r.price_rule,
            'unit_price': r.unit_price,
            'price': r.price,
            'product_code': r.product_code,
            'remark': r.remark,
        })

    return JsonResponse(rs, safe=False)


def query_detail_api(request):

    start = request.GET.get('start')
    end = request.GET.get('end')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')

    start = timezone.datetime.strptime(start, '%Y-%m-%d')
    end = timezone.datetime.strptime(end, '%Y-%m-%d')

    rs = []

    for i in range(500):
        start += timezone.timedelta(days=i)
        if start > end:
            break

        time_code = start.strftime('%Y%m%d')
        filter_args = {'time_code': time_code}

        if product_name:
            filter_args['product_name'] = product_name

            if result:
                filter_args['result'] = result

        qs = QueryDetail.objects.filter(**filter_args).limit(1000)

        for r in qs:
            rs.append({
                'time_code': r.time_code,
                'product_name': r.product_name,
                'result': r.result,
                'time': r.time,
                'query_id': r.query_id,
                'price_rule': r.price_rule,
                'unit_price': r.unit_price,
                'request': r.request,
                'response': r.response,
                'status_code': r.status_code,
                'return_time': r.return_time,
                'period': r.period,
                'product_code': r.product_code,
                'remark': r.remark,
            })

    return JsonResponse(rs, safe=False)
