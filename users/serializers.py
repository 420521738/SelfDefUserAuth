# -*- coding: utf-8 -*-
# author: kiven

from users.models import UserProfile, Department, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    departments = serializers.SlugRelatedField(many=True, queryset=Department.objects.all(), slug_field='name', allow_null=True)
    roles = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name', allow_null=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'username', 'email', 'departments', 'mobile', 'is_active', 'roles', 'valid_begin_time', 'valid_end_time', 'memo', 'password')
        extra_kwargs = {'password': {'write_only': False}}
        
    def create(self, validated_data):
        departments = validated_data.pop('departments')
        user = UserProfile.objects.create(**validated_data)
        user.departments = departments
        try:
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
