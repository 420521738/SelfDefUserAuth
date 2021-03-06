#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url
from users import views
from users import user

urlpatterns = [
    # 登录页
    url(r'^login/$',views.acc_login, name='login'),
    # 退出页
    url(r'^logout/$', views.logout, name='logout'),
    # 验证码功能
    url(r'^verifycode/$', views.verifycode),
    # 用户管理 开始
    url(r'^user/online/$', user.user_online_list, name='user_online_list'),
    url(r'^user/list/$', user.user_list, name='user_list'),
    url(r'^superuser/list/$', user.superuser_list, name='superuser_list'),
    url(r'^user/add/$', user.user_add, name='user_add'),
    url(r'^user/delete/(?P<ids>\d+)/$', user.user_del, name='user_del'),
    url(r'^user/edit/(?P<ids>\d+)/$', user.user_edit, name='user_edit'),
    url(r'^superuser/edit/(?P<ids>\d+)/$', user.superuser_edit, name='superuser_edit'),
    url(r'^reset/password/(?P<ids>\d+)/$', user.reset_password, name='reset_password'),
    url(r'^change/password/$', user.change_password, name='change_password'),
    # 用户个人信息
    url(r'^user/userinfo$', user.userinfo, name='userinfo'),
]

