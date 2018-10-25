#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return HttpResponse("OK <a href='/user/logout/'>退出登录</a>")