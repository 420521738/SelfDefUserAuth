#!/usr/bin/env python
#coding:utf-8

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, DepartmentViewSet, RoleViewSet

# Restful接口的配置方法，需要继承DefaultRouter，然后再依次注册用户接口，组接口，角色接口
usersrouter = DefaultRouter()
usersrouter.register(r'users', UserViewSet)
usersrouter.register(r'groups', DepartmentViewSet)
usersrouter.register(r'roles', RoleViewSet)