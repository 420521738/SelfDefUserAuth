#!/usr/bin/env python
#coding:utf-8

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, DepartmentViewSet, RoleViewSet

usersrouter = DefaultRouter()
usersrouter.register(r'users', UserViewSet)
usersrouter.register(r'groups', DepartmentViewSet)
usersrouter.register(r'roles', RoleViewSet)