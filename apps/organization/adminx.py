# -*- coding:utf-8 -*-
__author__ = 'wen'
__date__ = '2019/6/20 17:10'

from .models import CourseOrg,CityDict,Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ('name','desc','add_time',)  #
    search_fields = ('name','desc',)   #根据某一项查找
    list_filter = ('name','desc','add_time',)    #过滤器


class CourseOrgAdmin(object):
    list_display = ('name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time',)  ## list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    search_fields = ('name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city',)  # 根据某一项查找
    list_filter = ('name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time',)


class TeacherAdmin(object):
    list_display = ( 'org', 'name', 'work_years','work_company','work_position','points', 'click_num', 'fav_nums', 'image','add_time',)  ## list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    search_fields = ('org', 'name', 'work_years','work_company','work_position','points', 'click_num', 'fav_nums', 'image',)  # 根据某一项查找
    list_filter = ('org', 'name', 'work_years','work_company','work_position','points', 'click_num', 'fav_nums', 'image','add_time',)

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
