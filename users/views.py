#!/usr/bin/env python
#coding:utf-8

from rest_framework import viewsets
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django import utils
#引入绘图模块
from PIL import Image, ImageDraw, ImageFont
#引入随机函数模块
import random
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt

# 登录验证模块
def acc_login(request):
    # 如果请求的方式为POST，则为提交账号密码的操作
    if request.method == "POST":
        vcode = request.POST.get('vcode')
        session_code = request.session['verifycode']
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        # 判断用户的账号密码是否验证通过
        if user is not None:
            # 判断用户输入的验证码是否正确
            if vcode.upper() == session_code:
                # valid_end_time这个是账户的有效期结束时间
                if user.valid_end_time: #设置了end time
                    # 秋飞修改
                    #if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                    # 如果当前的时间大于账号的有效开始时间，并且当前时间小于用户的有效结束时间，就登录成功
                    if utils.timezone.now() > user.valid_begin_time and utils.timezone.now()  < user.valid_end_time:
                        auth.login(request,user)
                        # 这个很重要，是设置用户登录后session保存多久，这里设置了30分钟，30分钟后需要重新登录
                        request.session.set_expiry(60*30)
                        # 验证通过，返回首页
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        # 如果验证没通过，则返回登录页后，提示过期信息
                        return render(request,'login.html',{'login_err': '您的账号已过期，请联系管理员！'})
                # 秋飞修改
                #elif django.utils.timezone.now() > user.valid_begin_time:
                # 如果没有设置过期结束时间，那么则会查看当前时间是否比账号生效开始时间大，如果大就可以登录
                elif utils.timezone.now() > user.valid_begin_time:
                        auth.login(request,user)
                        # 这个很重要，是设置用户登录后session保存多久，这里设置了30分钟，30分钟后需要重新登录
                        request.session.set_expiry(60*30)
                        return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'users/login.html',{'login_err': '您输入的验证码错误，请重新输入！'})

        # 如果页面提交过来的账号密码没通过验证，则提示账号或者密码错误
        else:
            return render(request,'users/login.html',{'login_err': 'Wrong username or password!'})
    # 如果请求的方式不是post，那么直接返回login.html页面，也就是登录页
    else:
        return render(request, 'users/login.html')

# 账号退出模块    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def verifycode(request):
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20,100), random.randrange(20,100), 255)
    width = 100
    height = 35
    
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    
    #调用画笔的point()函数绘制噪点
    # range(0,100),指的是100个噪点，如果噪点越少，图片里面的字母数字识别得越清楚
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    
    #print '---------->',rand_str
    
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    
    #构造字体对象，这里需要注意，有很多地方说直接在这里写字体，但是直接写字体，不写绝对路径的话，程序会报错
    # windows下
    # ft = ImageFont.truetype("C:\Windows\Fonts\STZHONGS.TTF", 23)
    # linux下
    ft = ImageFont.truetype("STZHONGS.TTF", 23)
    
    #绘制4个字符
    draw.text((5, 2), rand_str[0], font=ft, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=ft, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=ft, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=ft, fill=fontcolor)
    
    #释放画笔
    del draw
    
    #将验证码存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    
    #内存文件操作
    buf = BytesIO()
    im = im.resize((80, 30))
    
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(),content_type="image/png")

        