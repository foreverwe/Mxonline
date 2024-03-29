from django.db import models

from datetime import datetime

from users.models import UserProfile

from courses.models import Course


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11,verbose_name=u"手机号")
    course_name = models.CharField(max_length=50,verbose_name=u"课程名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

class CourseComments(models.Model):
    """课程评论"""
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    comments = models.CharField(max_length=200,verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    # course = models.ForeignKey(Course,verbose_name=u"课程")
    # teacher =_
    # org =_
    # fav_type =_
    fav_id = models.IntegerField(default=0,verbose_name=u"数据id")   #fav_id指用户的id，IntegerField指另外一个表的ID
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"课程讲师")),default=1,verbose_name=u"收藏类型" )  #IntegerField指明用户的ID
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name



class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"接收用户")
    message = models.CharField(max_length=200,verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")   #判断是否已读
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")


    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"学习时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

