#!/usr/bin/env python
#coding:utf-8

from django.contrib import admin
from users import models
from django.contrib.auth.admin import UserAdmin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'roles', 'mobile', 'date_joined', 'is_active')
    search_fields = ['username']
    list_filter = ['roles', 'date_joined', 'is_active']
    
class DepartmenteAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ['name']
    list_filter = ['name']
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Department, DepartmenteAdmin)
admin.site.register(models.Role, RoleAdmin)