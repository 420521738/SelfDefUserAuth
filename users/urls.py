#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url
from users.routerApi import usersrouter
from users import views

urlpatterns = [
    # Restful 用户信息修改接口
    url(r'^api/', include(usersrouter.urls)),
    # 登录页
    url(r'^login/$',views.acc_login, name='login'),
    # 退出页
    url(r'^logout/$', views.logout, name='logout'),
    # 验证码功能
    url(r'^verifycode/$', views.verifycode),
]

