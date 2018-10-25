#!/usr/bin/env python
#coding:utf-8

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django import utils


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        username 是唯一标识，没有会报错
        """

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )
        user.set_password(password)  # 检测密码合理性
        user.save(using=self._db)  # 保存密码
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username,
                                password=password,
                                )
        user.is_admin = True  # 比创建用户多的一个字段
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    # This 用户信息组成：用户名，邮箱，部门，手机号，创建时间，是否启用，是否是管理员，角色，帐号有效开始时间，帐号有效结束时间，备注
    username = models.CharField(max_length=32, unique=True, db_index=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    departments = models.ManyToManyField('Department', max_length=32, default=None, blank=True, null=True, verbose_name=u'部门')
    mobile = models.CharField(u'手机', max_length=32,default=None,blank=True,null=True)
    date_joined = models.DateTimeField(blank=True, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roles = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'角色')
    valid_begin_time = models.DateTimeField(default=utils.timezone.now)
    valid_end_time = models.DateTimeField(blank=True,null=True)
    memo = models.TextField(u'备注', blank=True,null=True,default=None)

    USERNAME_FIELD = 'username'  # 必须有一个唯一标识--USERNAME_FIELD
    #REQUIRED_FIELDS = ['email']
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.username
    
    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u"用户信息"
        
    def __unicode__(self):
        return self.username

    objects = UserManager()  # 创建用户


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'部门')
    desc = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'组'
        verbose_name_plural = u'部门'


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'角色')
    desc = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'角色'
        verbose_name_plural = u'角色'