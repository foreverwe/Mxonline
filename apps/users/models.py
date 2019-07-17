from django.db import models
from django.contrib.auth.models import  AbstractUser  #django自身提供的User表，
from   datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default='')
    birthday = models.DateField(verbose_name=u"生日",null=True)
    gender = models.CharField(max_length=10,choices=(("male",u"男"),("female",u"女")),default="female",verbose_name=u"性别")   #这里性别可以选择，所以用choices
    address = models.CharField(max_length=100,verbose_name=u"地址",default='')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u"手机号")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,verbose_name=u"图像")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):  #重载unicode方法（打印UerProfile实例化对象时的字符串）
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(max_length=50,choices=(("register",u"注册"),("forget",u"找回密码")),verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")  #注意去掉括号（得到的是实例化时的时间，否则得到编译的时间）

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  '{0}({1})'.format(self.code,self.email)   #重载unicode方法


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图")
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
