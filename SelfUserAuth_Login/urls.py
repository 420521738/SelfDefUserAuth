#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from SelfUserAuth_Login import views

urlpatterns = [
    # This Admin后台管理url入口
    url(r'^admin/', admin.site.urls),
    # This 定义首页入口
    url(r'^$',views.index, name="index"),
    # This 定义user相关的所有功能入口
    url(r'^user/', include('users.urls')),
]

