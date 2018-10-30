#!/usr/bin/env python
#coding:utf-8

from django.contrib import admin
from users import models
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# 这里定义的是django admin管理后台展示的内容
# 在django admin管理后台中展示用户信息表

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.UserProfile
        fields = ('email','token')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """ 
    
    # 接口在django.contrib.auth.admin.user_change_password文件里，但是并不能直接调用，因为多了一个change字段
    # 正确的修改指定用户的链接是/admin/assets/userprofile/4/password/，但是在class里获取不到用户的id,所以就想到了url重定向，在MadKing的url里
    password = ReadOnlyPasswordHashField(label="Password",
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    'using <a href="password">密码修改</a>.'))

    class Meta:
        model = models.UserProfile
        fields = ('email', 'password','is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserProfileAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','name','email','department','is_admin','is_active')
    list_filter = ('is_admin',)
    # 这里是添加完用户后，因为添加的用户信息比较简单，添加完后会显示以下这些详细字段可以补充填写的
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        ('Personal info', {'fields': ('department','tel','mobile','memo')}),
        ('API TOKEN info', {'fields': ('token',)}),
        ('Permissions', {'fields': ('is_active','is_admin')}),
        ('账户有效期', {'fields': ('valid_begin_time','valid_end_time')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # 这里是用户管理，添加新用户的时候，显示什么字段是显示出来首次需要填写的；
    # 'email', 'name', 'password1', 'password2','is_active','is_admin'这些字段是添加用户时需要写的
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2','is_active','is_admin')}
        ),
    )
    search_fields = ('email','name',)
    ordering = ('name',)
    filter_horizontal = ()

# 需要在admin中进行注册，才能在django admin的管理后台中看到
# 如果register后台只加model，那么仅仅会显示一个model中定义的self.username或者其他
admin.site.register(models.UserProfile, UserProfileAdmin)