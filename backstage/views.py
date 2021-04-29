from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from backstage import models

# Create your views here.


def baseTest(request):
    """
    测试母版
    :param request:
    :return:
    """
    return render(request,'common/base.html')


def login(request):
    """
    管理员登录
    :param request:
    :return:
    """
    return render(request,'login/login.html')


def loginHandle(request):
    """
    管理员登录处理
    :param request:
    :return:
    """
    username =request.POST.get("username")
    pwd =request.POST.get("pwd")
    # 查找用户表 判断用户信息是否正确
    print(username,pwd)

    return JsonResponse({"code":0,"msg":"success"})


def index(request):
    """
    后台首页
    :param request:
    :return:
    """
    return render(request,'index/index.html')


def goodslist(request):
    """
    商品列表页面
    :param request:
    :return:
    """
    return render(request,'goods/goodslist.html')



