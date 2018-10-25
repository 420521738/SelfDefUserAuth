#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required


# 加了登录装饰器，想要访问首页，需要先登录，如未登录，则调转到settings中定义的/user/login/这个url中去
@login_required
def index(request):
    return HttpResponse("OK <a href='/user/logout/'>退出登录</a>")