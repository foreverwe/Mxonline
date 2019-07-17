# -*- coding:utf-8 -*- #
__author__ = 'wen'
__date__ = '2019/6/20 17:44'


from .models import UserMessage,UserAsk,UserCourse,UserFavorite,CourseComments
import xadmin



class UserAskAdmin(object):

    # list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('name', 'mobile','course_name', 'add_time')  #
    search_fields = ('name', 'mobile','course_name',)  # 根据某一项查找
    list_filter = ('name', 'mobile','course_name', 'add_time')  # 过滤器

class CourseCommentsAdmin(object):

    list_display = ('user', 'course','comments', 'add_time')  #
    search_fields = ('user', 'course','comments', )  # 根据某一项查找
    list_filter = ('user', 'course','comments', 'add_time')  # 过滤器


class UserFavoriteAdmin(object):
    list_display = ('user', 'fav_id','fav_type', 'add_time')  #
    search_fields = ('user', 'fav_id','fav_type', )  # 根据某一项查找
    list_filter = ('user', 'fav_id','fav_type', 'add_time')  # 过滤器


class UserMessageAdmin(object):
    list_display = ('user', 'message','has_read', 'add_time')  #
    search_fields = ('user', 'message','has_read', )  # 根据某一项查找
    list_filter = ('user', 'message','has_read', 'add_time')  # 过滤器


class UserCourseAdmin(object):

    list_display = ('user', 'course', 'add_time')  #
    search_fields = ('user', 'course')  # 根据某一项查找
    list_filter = ('user', 'course', 'add_time')  # 过滤器


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
