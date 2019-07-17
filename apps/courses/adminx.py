# -*- coding:utf-8 -*-
__author__ = 'wen'
__date__ = '2019/6/20 12:45'

from datetime import datetime

from .models import Course,Lesson,Video,CourseResource

import xadmin



class CourseAdmin(object):

    list_display = ('name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image',
                    'click_number', 'add_time',)  ## list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    search_fields = ('name', 'desc', 'detail', 'degree', 'students','fav_nums', 'image','click_number',)  # 根据某一项查找
    list_filter = ('name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_number','add_time')  # 过滤器


class LessonAdmin(object):
    # list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('course', 'name', 'add_time')  #
    search_fields = ('course', 'name',)  # 根据某一项查找
    list_filter = ('course__name', 'name', 'add_time')  # 过滤器   'course__name'指定外键
    def __str__(self):
        return self.name


class VideoAdmin(object):
    # list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('lesson', 'name', 'add_time')  #
    search_fields = ('lesson', 'name',)  # 根据某一项查找
    list_filter = ('lesson', 'name', 'add_time')  # 过滤器


class CourseResourceAdmin(object):
    # list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('course', 'name','download', 'add_time')  #
    search_fields = ('course', 'name','download')  # 根据某一项查找
    list_filter = ('course', 'name','download', 'add_time')  # 过滤器


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
