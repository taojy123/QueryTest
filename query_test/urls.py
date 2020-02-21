"""query_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('detail/', detail),
    path('api/query_statistics/', api_query_statistics),
    path('api/year_statistics/', api_year_statistics),
    path('api/month_statistics/', api_month_statistics),
    path('api/day_statistics/', api_day_statistics),
    path('api/query_detail/', api_query_detail),
    path('api/best_day/', api_best_day),
    path('api/best_month/', api_best_month),
    path('api/total_year/', api_total_year),
    path('api/trail/', api_trail),
    path('admin/', admin.site.urls),
]
