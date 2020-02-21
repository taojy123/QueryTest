from django.contrib import admin

from app import models


@admin.register(models.Trial)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'name', 'mobile', 'company_name', 'company_domain',
                    'company_city', 'company_address', 'company_email']


