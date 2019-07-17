# -*- coding:utf-8 -*-
__author__ = 'wen'
__date__ = '2019/6/24 21:08'

from random import Random

from users.models import EmailVerifyRecord   #

from  CourseEngine.settings import EMAIL_FROM   #

from django.core.mail import send_mail   #django内部自带的发送邮箱


def random_str(randomlength = 8):  #生成随机字符串
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type = 'register'):  #定义发送邮件的基础函数
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下列链接激活你的账号：httl://127.0.0.1:8000/activate/{0}".format(code)

        send_status =  send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass