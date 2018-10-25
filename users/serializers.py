# -*- coding: utf-8 -*-
# author: kiven

from users.models import UserProfile, Department, Role
from rest_framework import serializers


# Restful 用户接口类定义使用的序列化的类
class UserSerializer(serializers.ModelSerializer):
    departments = serializers.SlugRelatedField(many=True, queryset=Department.objects.all(), slug_field='name', allow_null=True)
    roles = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name', allow_null=True)

    class Meta:
        model = UserProfile
        # This 定义api接口信息中展示的字段以及深度，这里并未定义深度，只定义展示什么字段
        fields = ('url', 'id', 'username', 'email', 'departments', 'mobile', 'is_active', 'roles', 'valid_begin_time', 'valid_end_time', 'memo', 'password')
        # write_only 需要设置为True
        extra_kwargs = {'password': {'write_only': True}}
    
    # This 定义如果是创建用户，则执行create函数
    def create(self, validated_data):
        departments = validated_data.pop('departments')
        user = UserProfile.objects.create(**validated_data)
        user.departments = departments
        try:
            # This 对密码进行加密，如果没有这个步骤，那么用户存的密码就是明文的，在登录时总会提示帐号或者密码错误
            user.set_password(validated_data['password'])
        except:
            pass
        user.save()
        return user

    def update(self, instance, validated_data):
        departments = validated_data.pop('departments')
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.roles = validated_data.get('roles', instance.roles)
        instance.valid_begin_time = validated_data.get('valid_begin_time', instance.valid_begin_time)
        instance.valid_end_time = validated_data.get('valid_end_time', instance.valid_end_time)
        instance.memo = validated_data.get('memo', instance.memo)
        try:
            # This 对密码进行加密，如果没有这个步骤，那么用户存的密码就是明文的，在登录时总会提示帐号或者密码错误
            instance.set_password(validated_data['password'])
        except Exception as e:
            pass
        instance.departments = departments
        instance.save()
        return instance


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'id', 'name', 'desc')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'id', 'name', 'desc')
