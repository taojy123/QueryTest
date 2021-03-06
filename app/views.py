import calendar

from cassandra.cqlengine import CQLEngineException
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render
from django.utils import timezone

from app.cassandra_models import QueryStatistics, QueryDetail2, Best, Total
from app.models import Trial


def index(request):
    return render(request, 'index.html', locals())


def detail(request):
    return render(request, 'detail.html', locals())


def api_query_statistics(request):

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


def api_year_statistics(request):

    year = request.GET.get('year')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')
    period = request.GET.get('period')

    if not year:
        return HttpResponseBadRequest('miss year')

    filter_args = {}

    if product_name:
        filter_args['product_name'] = product_name

        if result:
            filter_args['result'] = result

            if period:
                filter_args['period'] = period
    rs = []
    for month in range(1, 13):
        time_code = '%s%02d' % (year, month)
        filter_args['time_code'] = time_code

        qs = QueryStatistics.objects.filter(**filter_args).limit(1000)

        count = 0
        for r in qs:
            count += r.count

        rs.append({
            'time_code': time_code,
            'count': count,
        })

    return JsonResponse(rs, safe=False)


def api_month_statistics(request):

    year = request.GET.get('year')
    month = request.GET.get('month')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')
    period = request.GET.get('period')

    if not year:
        return HttpResponseBadRequest('miss year')

    if not month:
        month = timezone.datetime.now().month - 1
        if month <= 0:
            month = 12
        month = '%02d' % month

    filter_args = {}

    if product_name:
        filter_args['product_name'] = product_name

        if result:
            filter_args['result'] = result

            if period:
                filter_args['period'] = period

    days = calendar.monthrange(int(year), int(month))[1]
    rs = []
    for day in range(1, days + 1):
        time_code = '%s%s%02d' % (year, month, day)
        filter_args['time_code'] = time_code

        qs = QueryStatistics.objects.filter(**filter_args).limit(1000)

        count = 0
        for r in qs:
            count += r.count

        rs.append({
            'time_code': time_code,
            'count': count,
        })

    return JsonResponse(rs, safe=False)


def api_day_statistics(request):

    start = request.GET.get('start')
    end = request.GET.get('end')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')

    start = timezone.datetime.strptime(start, '%Y-%m-%d')
    end = timezone.datetime.strptime(end, '%Y-%m-%d')

    rs = []

    for i in range(500):
        day = start + timezone.timedelta(days=i)
        if day > end:
            break

        time_code = day.strftime('%Y%m%d')
        filter_args = {'time_code': time_code}

        if product_name:
            filter_args['product_name'] = product_name

            if result:
                filter_args['result'] = result

        qs = QueryStatistics.objects.filter(**filter_args).limit(1000)
        count = 0
        for r in qs:
            count += r.count

        rs.append({
            'time_code': time_code,
            'count': count,
        })

    return JsonResponse(rs, safe=False)


def api_query_detail(request):

    start = request.GET.get('start')
    end = request.GET.get('end')
    product_name = request.GET.get('product_name')
    result = request.GET.get('result')

    start = timezone.datetime.strptime(start, '%Y-%m-%d')
    end = timezone.datetime.strptime(end, '%Y-%m-%d')

    rs = []

    for i in range(500):
        day = start + timezone.timedelta(days=i)
        if day > end:
            break

        time_code = day.strftime('%Y%m%d')
        filter_args = {'time_code': time_code}

        if product_name:
            filter_args['product_name'] = product_name

            if result:
                filter_args['result'] = result

        qs = QueryDetail2.objects.filter(**filter_args).limit(1000)

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


def api_best_day(request):
    product_name = request.GET.get('product_name')
    try:
        r = Best.objects.filter(product_name=product_name, category='日最高访问量').limit(1)[0]
    except IndexError as e:
        return HttpResponseNotFound()
    r = {
        'value': r.value,
        'time': r.time,
    }
    return JsonResponse(r)


def api_best_month(request):
    product_name = request.GET.get('product_name')
    try:
        r = Best.objects.filter(product_name=product_name, category='月最高访问量').limit(1)[0]
    except IndexError as e:
        return HttpResponseNotFound()
    r = {
        'value': r.value,
        'time': r.time,
    }
    return JsonResponse(r)


def api_total_year(request):
    product_name = request.GET.get('product_name')
    try:
        year_code = timezone.now().strftime('%Y')
        r = Total.objects.filter(product_name=product_name, time_code=year_code).limit(1)[0]
    except IndexError as e:
        return HttpResponseNotFound()
    r = {
        'value': r.value,
        'time': r.time,
    }
    return JsonResponse(r)


def api_trail(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        name = request.POST['name']
        mobile = request.POST['mobile']
        company_name = request.POST['company_name']
        company_domain = request.POST['company_domain']
        company_city = request.POST['company_city']
        company_address = request.POST['company_address']
        company_email = request.POST['company_email']
        detail = request.POST['detail']
        Trial.objects.create(
            product_name=product_name,
            name=name,
            mobile=mobile,
            company_name=company_name,
            company_domain=company_domain,
            company_city=company_city,
            company_address=company_address,
            company_email=company_email,
            detail=detail,
        )
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])
