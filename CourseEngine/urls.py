"""CourseEngine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include   #
from django.contrib import admin
from django.views.generic import TemplateView  #
import xadmin
# from users.views import user_login   # 导入封装的函数
from users.views import LoginView,RegisterView    # 导入封装的类
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name="index.html"),name="index"),
    url('^login/$', LoginView.as_view(), name="login"),   #封装类的url写法
    url('^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    # url('^login/$',user_login,name="login")     #封装函数的url写法
# url('^login/$',TemplateView.as_view(template_name="login.html"),name="login")
]
