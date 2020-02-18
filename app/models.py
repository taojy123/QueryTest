from django.db import models


class Trial(models.Model):
    product_name = models.CharField(max_length=128, blank=True, verbose_name='产品名称')
    name = models.CharField(max_length=128, blank=True, verbose_name='用户姓名')
    mobile = models.CharField(max_length=128, blank=True, verbose_name='联系手机')
    company_name = models.CharField(max_length=128, blank=True, verbose_name='单位名称')
    company_domain = models.CharField(max_length=128, blank=True, verbose_name='单位领域')
    company_city = models.CharField(max_length=128, blank=True, verbose_name='单位省市')
    company_address = models.CharField(max_length=128, blank=True, verbose_name='详细地址')
    company_email = models.CharField(max_length=128, blank=True, verbose_name='单位邮箱')
    detail = models.CharField(max_length=128, blank=True, verbose_name='需求描述')

