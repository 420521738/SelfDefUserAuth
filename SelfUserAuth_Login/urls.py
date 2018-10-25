#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from SelfUserAuth_Login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name="index"),
    url(r'^user/', include('users.urls')),
]

