# 自定义user认证模块、用户登录及验证码模块 #

注意：本工具基于 python3.5.4版本，Django1.11.14版本前提进行开发。本工具开发调试均在谷歌浏览器下进行，所以建议使用谷歌浏览器进行访问。测试后发现，火狐浏览器也是可以正常访问的，所以首选推荐谷歌浏览器，其次是火狐浏览器。

本项目主要是自定义user认证模块，使用自定义的用户模块，编写登录以及验证码功能，用户信息修改使用标准的restful接口。至于为什么要自定义django的user模块，应该也不用多说了，django自定义的user模块字段相对较少，而且不能灵活修改，所以自定义的好处就是你想怎么改就怎么改。

作者QQ：420521738，添加时请备注原因，很欢迎各位加我一起探讨学习。


## 项目介绍

### 1.登录

* 帐号登录功能，结合了验证码输入功能，防止恶意尝试密码行为。

##### 登录效果截图：
![Login](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/Login.png)


### 2.Restful 接口展示

* 现在用得比较多的restful接口，web上来给大家展示一下。

##### restful入口效果截图：
![RestfulApi_Index](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/RestfulApi_Index.png)
##### restful查询信息效果截图：
![RestfulApi_Info](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/RestfulApi_Info.png)
##### restful提交信息效果截图：
![RestfulApi_POST](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/RestfulApi_POST.png)


### 3.Django Admin 管理后台自定义展示

* Django Admin管理后台是可以自定义展示指定内容，可以定义展示什么内容，以及该内容的某些字段，还可以定义该内容的过滤条件以及搜索字段。

##### 自定义django admin的入口效果截图：
![DjangoAdmin_Index](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/DjangoAdmin_Index.png)
##### 自定义django admin的用户表效果截图：
![DjangoAdmin_User](https://github.com/420521738/SelfUserAuth_Login/blob/master/screenshots/DjangoAdmin_User.png)
