# -*- coding:utf-8 -*-
__author__ = 'wen'
__date__ = '2019/6/22 14:52'

from django import forms

from captcha.fields import CaptchaField
class LoginForm(forms.Form):

    username = forms.CharField(required=True)   #required=True表示该字段必须为非空
    password = forms.CharField(required=True ,min_length=5)


class RegisterForm(forms.Form):    #对注册表单的验证
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid':u"验证码错误"})
