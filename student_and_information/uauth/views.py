from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from uauth.models import User


def regist(request):
    if request.method == "GET":
        return render(request,'register.html')
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        password = make_password(password) # 对password进行加密

        User.objects.create(
            u_name=name,
            u_password=password
        )
        return HttpResponseRedirect('/uauth/login/')

def login(request):
    if request.method == "GET":
        return  render(request,'login.html')
    if request.method == "POST":
        # 如果登录成功，绑定参数到cookie中，set_cookie()
        name = request.POST.get("name")
        password = request.POST.get("password")

        if User.objects.filter(u_name=name).exists(): # 如果用户名存在
            user = User.objects.get(u_name=name)
            if check_password(password,user.u_password):
                ticket = 'lalala'
                # 绑定令牌到cookie里面
                response = HttpResponse()
                response.set_cookie('ticket',ticket)
                # 存在数据库中
                user.u_ticket = ticket
                user.save()
                return response
            else:
                return HttpResponse("用户密码错误！！")
        else:
            return HttpResponse("用户不存在！！")

def logout(request):
    if request.method == "GET":
        response = HttpResponse()
        response.delete_cookie('ticket')
        return response

