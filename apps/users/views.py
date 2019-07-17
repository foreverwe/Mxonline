from django.shortcuts import render
from django.contrib.auth import authenticate, login #
from django.contrib.auth.backends import ModelBackend   #
from .models import UserProfile   #
from django.db.models import Q   #并集，用户名或邮箱
from django.views.generic.base import View    #基于类继承完善login
from .forms import LoginForm,RegisterForm   #对表单中的内容做出判断
from utils.email_send import send_register_email

from django.contrib.auth.hashers import make_password   #对于密码部分，对明文进行加密
# Create your views here.
class CustomBackend(ModelBackend):   #自定义登陆时的方法，用户名或邮箱
    def authenticate(self,username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username) )  ##交集用逗号就行
            if user.check_password(password):   #比对密码
                return user

        except Exception as e:
            return None

# ----封装类的注册页面
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})   #生成的图片验证码

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name,"register")
            pass
        #     return render(request, "login.html", {"msg": "用户名或密码错误"})
        # else:
        #     return render(request,'register.html',{"register_form":register_form})


        # class RegisterView(View):
        #     def get(self, request):
        #         register_form = RegisterForm()
        #         return render(request, "register.html", {'register_form': register_form})
        #
        #     def post(self, request):
        #         register_form = RegisterForm(request.POST)
        #         if register_form.is_valid():
        #             user_name = request.POST.get("email", "")
        #             if UserProfile.objects.filter(email=user_name):
        #                 return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
        #             pass_word = request.POST.get("password", "")
        #             user_profile = UserProfile()
        #             user_profile.username = user_name
        #             user_profile.email = user_name
        #             user_profile.is_active = False
        #             user_profile.password = make_password(pass_word)
        #             user_profile.save()
        #
        #             # 写入欢迎注册消息
        #             user_message = UserMessage()
        #             user_message.user = user_profile.id
        #             user_message.message = "欢迎注册慕学在线网"
        #             user_message.save()
        #
        #             send_register_email(user_name, "register")
        #             return render(request, "login.html")
        #         else:
        #             return render(request, "register.html", {"register_form": register_form})


# ----封装类的登陆页面
class LoginView(View):     #  ==def user_login(request):   下边
    def get(self, request):    #   ==request.method == "GET":
        return render(request, "login.html", {})

    def post(self,request):     #  ==request.method == "POST":
        login_form = LoginForm(request.POST)   #实例化对象   html文件中两字段的name和Login_Form中的两变量名必须一致
        if login_form.is_valid()  : #判断提交的表单是否符合要求
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username = user_name, password = pass_word)  #注意变量名
            if user is not None:
                login(request, user)      #login为内部命令，所以上边函数不能同名定义  #这里利用的是session和cookie的机制
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})

        else:
            return render(request, "login.html", {"login_form":login_form})   ##返回login_form中的错误信息



#  #封装函数的登陆页面
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#         user = authenticate(username = user_name, password = pass_word)  #注意变量名
#         if user is not None:
#             login(request, user)      #login为内部命令，所以上边函数不能同名定义
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg":"用户名或密码错误"})
#     else:
#         # elif request.method == "GET":
#         return render(request, "login.html", {})

