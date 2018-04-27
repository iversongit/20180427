from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
def logIN(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        # 验证用户名和密码，返回用户对象
        user = authenticate(username=username,password=password)
        if user: # 如果用户对象存在
            login(request,user) # 用户登录
            return HttpResponseRedirect("/loginapp/index/")
        else:
            return HttpResponse("用户名或密码错误")

def logOUT(request):
    logout(request) # 注销用户
    return HttpResponseRedirect("/loginapp/login/")

def createUSER(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        if User.objects.filter(username=username):
            return HttpResponse("该用户名已存在")
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            return HttpResponse("创建成功")

def changePWD(request):
    if request.method == "GET":
        return render(request,"changepwd.html")
    if request.method == "POST":
        username = request.POST.get("name")
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        user = authenticate(username=username, password=oldpassword)
        if user:  # 如果用户对象存在
            user.set_password(newpassword) # 设置新密码
            user.save()
            return HttpResponse("密码修改成功")

def index(request):
    if not request.user.is_authenticated():
        return HttpResponse("请您先登录！！")
    else:
        return render(request,"index.html")