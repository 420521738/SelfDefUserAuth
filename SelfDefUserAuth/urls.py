#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from SelfDefUserAuth import views
from users import user

urlpatterns = [
    # 添加这条url的前提是由于用户认证模块是用自己修改的，修改指定id用户的密码时，会带有change的多余字段，需要把change多余字段删除，才是正确的密码修改请求
    url(r'^admin/users/userprofile/(\d+)/change/password/', views.urlchange_passwd),
    # This Admin后台管理url入口
    url(r'^admin/', admin.site.urls),
    # This 定义首页入口
    url(r'^$', user.user_list, name='index'),
    # This 定义user相关的所有功能入口
    url(r'^user/', include('users.urls')),
]

