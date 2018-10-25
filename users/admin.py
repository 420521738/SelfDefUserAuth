#!/usr/bin/env python
#coding:utf-8

from django.contrib import admin
from users import models
from django.contrib.auth.admin import UserAdmin


# 这里定义的是django admin管理后台展示的内容
# 在django admin管理后台中展示用户信息表
class UserProfileAdmin(admin.ModelAdmin):
    # This 展示的字段有哪些
    list_display = ('username', 'email', 'roles', 'mobile', 'date_joined', 'is_active')
    # This 可以设置查询字段
    search_fields = ['username']
    # This 可以设置过滤字段
    list_filter = ['roles', 'date_joined', 'is_active']
    
class DepartmenteAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ['name']
    list_filter = ['name']
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ['name']
    list_filter = ['name']

# 需要在admin中进行注册，才能在django admin的管理后台中看到
# 如果register后台只加model，那么仅仅会显示一个model中定义的self.username或者其他
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Department, DepartmenteAdmin)
admin.site.register(models.Role, RoleAdmin)