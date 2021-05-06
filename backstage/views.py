from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from backstage import models
from utils.tools import *
# Create your views here.


def baseTest(request):
    """
    测试母版
    :param request:
    :return:
    """
    return render(request,'common/base.html')


def upload(request):
    """
    图片上传接口
    :param request:
    :return:
    """
    if request.FILES.get("file"):
        src =uploadOss(request.FILES.get("file"))
        return JsonResponse({"code":0,"msg":"success","data":{"src":src}})

    return JsonResponse({"code":1,"msg":"no files"})


"""
登录模块
"""

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


"""
首页模块
"""

def index(request):
    """
    后台首页
    :param request:
    :return:
    """
    return render(request,'index/index.html')


"""
商品模块
"""


def goodslist(request):
    """
    商品列表页面
    :param request:
    :return:
    """
    return render(request,'goods/goodslist.html')


def addgoods(request):
    """
    商品发布页面
    :param request:
    :return:
    """
    return render(request,'goods/addgoods.html')


def goodsCategory(request):
    """
    商品分类页面
    :param request:
    :return:
    """
    return render(request,'goods/goodscategory.html')


def addGoodsCategory(request):
    """
    添加商品分类页面
    :param request:
    :return:
    """
    return render(request,'goods/addgoodscategory.html')


def goodsAttr(request):
    """
    商品属性页面
    :param request:
    :return:
    """
    return render(request,'goods/goodsAttribute.html')


def addgoodsAttr(request):
    """
    添加商品属性页面
    :param request:
    :return:
    """
    return render(request,'goods/addgoodsAttr.html')


def goodsRecommend(request):
    """
    商品推荐模块
    :param request:
    :return:
    """
    return render(request,'goods/goodsRecommend.html')


def goodsRecomList(request):
    """
    商品推荐列表
    :param request:
    :return:
    """
    return render(request,'goods/goodsRecomList.html')


def goodsSpecList(request):
    """
    商品规格
    :param request:
    :return:
    """
    return render(request,'goods/goodsSpecList.html')


