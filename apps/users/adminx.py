# -*- coding:utf-8 -*-
__author__ = 'wen'
__date__ = '2019/6/20 10:57'

import xadmin

from xadmin import views   #

from datetime import datetime

from .models import EmailVerifyRecord,Banner   #从数据库模型中导入表
# UserProfile在admin时已经注册到admin


#django后台的全栈配置
class BaseSetting(object):     #主题
    enable_themes = True   #开启主题功能
    use_bootswatch = True   #


class GlobalSettings(object):   #logo和页脚的配置
    site_title = "慕学在线管理系统"
    site_footer = "慕学在线网"
    menu_style  = "accordion"   #可收起 每个app中的内容


class EmailVerifyRecordAdmin(object):   #继承最顶层的类

#list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('code','email','send_type','send_time')  #
    search_fields = ('code','email','send_type',)   #根据某一项查找
    list_filter = ('code','email','send_type','send_time')    #过滤器


class BannerAdmin(object):   #继承最顶层的类

#list_display为元组形式或列表，定义我们在后台列表中想显示的内容
    list_display = ('title','image','url','index','add_time')  #
    search_fields = ('title','image','url','index',)   #根据某一项查找
    list_filter = ('title','image','url','index','add_time')    #过滤器

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)   #model和admin进行关联注册
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)   #全栈配置和admin进行关联注册
xadmin.site.register(views.CommAdminView,GlobalSettings)    #第一个必须照写，第二个为类名