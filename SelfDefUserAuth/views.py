#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# 加了登录装饰器，想要访问首页，需要先登录，如未登录，则调转到settings中定义的/user/login/这个url中去
@login_required
def index(request):
    return HttpResponse("OK <a href='/user/logout/'>退出登录</a>")

# 后台用户信息里面，指定id修改指定用户的密码功能，由于用户认证写过了，如果还用原来的密码修改请求url，则会多一个change字段，需要把这个change字段删除，才能正常修改密码
def urlchange_passwd(request,userid):
    request_path = request.path.replace('/change','')
    return HttpResponseRedirect(request_path)