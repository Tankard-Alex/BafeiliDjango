import datetime
import json

from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from backstage import models
from django.db.models import Count
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
    # 相册id，用于多图片上传
    album_id = request.POST.get("album_id")
    try:
        if not album_id:
            # 单张图片上传
            upload_info = uploadOss(request.FILES.get("file"))
            print(upload_info)
            src = upload_info.get("img_src")
            return JsonResponse({"code": 0, "msg": "success", "data": {"src": src}})
        # 多张图片上传
        file_info = uploadOss(request.FILES.get("file"))
        pic_name = file_info.get("pic_name")  # 图片名称
        pic_spec = file_info.get("pic_size")  # 图片规格(尺寸
        pic_cover = file_info.get("img_src")  # 图片地址
        new_pic = models.SysAlbumPicture(album_id=album_id, pic_name=pic_name, pic_cover=pic_cover, pic_spec=pic_spec,
                                         pic_size=pic_spec,upload_time=int(time.time()))
        new_pic.save()
        return JsonResponse({"code": 0, "msg": "success"})
    except:
        return JsonResponse({"code":1,"msg":"error"})


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
    # 渲染页面的情况
    print(request.method)
    if request.method == "GET":
        return render(request, 'goods/goodslist.html')
    # 请求商品列表数据的情况

    # 读取商品数据
    goods_list =list(models.Goods.objects.all().values("goods_id","goods_name","picture","sale_price","stock","sell_count","create_time"))
    # 格式化相册图片数据
    pic_list =models.SysAlbumPicture.objects.all().values("pic_id","pic_cover")
    pic_info ={i["pic_id"]: i["pic_cover"] for i in pic_list}
    # 处理得到的商品数据列表
    for goods in goods_list:
        goods["picture"] =pic_info[goods["picture"]]
        goods["create_time"] =datetime.datetime.fromtimestamp(goods["create_time"]).strftime("%Y-%m-%d")

    # 分页处理
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit")
    paginator = Paginator(goods_list, limit)  # 分页器对象
    page_obj = paginator.page(page)  # 当前页的page对象

    # 整理出返回的数据
    ret_data={
        "code":0
        ,"msg":""
        , "count": paginator.num_pages * 10
        ,"data":list(page_obj)

    }

    return JsonResponse(ret_data)


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
    # 获取商品分类的数据
    cate_list =list(models.GoodsCategory.objects.filter(pid=0).values("category_id","category_name","pid","is_visible","sort"))
    for cate in cate_list:
        cate["sec_cate"] =list(models.GoodsCategory.objects.filter(pid=cate["category_id"]).values("category_id","category_name","pid","is_visible","sort"))
        cate["is_visible_ch"] ="是" if cate["is_visible"] == 1 else "否"
    print(cate_list)
    return render(request,'goods/goodscategory.html',context={"cate_list":cate_list,"cate_list_json":json.dumps(cate_list)})


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


def albumList(request):
    """
    相册管理
    :param request:
    :return:
    """
    # 整理相册列表数据
    album_list =list(models.SysAlbum.objects.all().values("album_id","album_name"))
    keywords =request.POST.get("keywords")
    if keywords:
        album_list = list(models.SysAlbum.objects.filter(album_name__contains=keywords).values("album_id", "album_name"))
    # 通过聚合函数查询每个相册中有多少张图片 并构建出字典推导式便于查询
    count_info =models.SysAlbumPicture.objects.values("album_id").annotate(count=Count('album_id'))
    count_dic ={i["album_id"]:i["count"] for i in count_info}
    # 在每个相册中选一张图片作为封面 并构建出字典推导式便于查询
    cover_info = models.SysAlbumPicture.objects.values("album_id", "pic_cover").distinct()
    cover_dic = {i["album_id"]: i["pic_cover"] for i in cover_info}
    for item in album_list:
        # 该相册中图片的数量
        picture_num =int(item["album_id"])
        try:
            num =count_dic[picture_num]
        except:
            num=0
        item["album_count"] =num
        if num > 0:
            item["album_cover"] =cover_dic[int(item["album_id"])]
        # 如果该相册没有照片则封面为指定的默认图片
        else:
            item["album_cover"] ="http://xcx.bafelli.com/public/admin/images/album/album_cover_default.png"
    paginator = Paginator(album_list, 12)  # 分页器对象
    page_obj = paginator.page(1)  # 当前页的page对象

    # 浏览器发起的请求
    if request.method == "GET":
        return render(request,'goods/albumList.html',context={"count":paginator.num_pages*10,"album_list":page_obj})
    # 前台分页触发的ajax请求
    try:
        page =request.POST.get("page",1) # 页码
        keywords =request.POST.get("keywords","")
        page_obj =paginator.page(page)

        return JsonResponse({"code":0,"msg":"success","album_list":list(page_obj),"keywords":keywords,"count":paginator.num_pages*10})
    except:
        return JsonResponse({"code":1,"msg":"error"})


def addAlbum(request):
    """
    添加相册
    :param request:
    :return:
    """

    album_name =request.POST.get("album_name")  # 相册名称
    sort =request.POST.get("sort")  # 排序
    # 判断该相册是否存在
    exist_count =len(list(models.SysAlbum.objects.filter(album_name=album_name)))
    if exist_count == 0:
        # 如果该相册名称不存在则创建
        try:
            album_new = models.SysAlbum(album_name=album_name, is_default=0, sort=sort,create_time=time.time())
            album_new.save()
            return JsonResponse({"code": 0, "msg": "创建成功"})
        except:
            return JsonResponse({"code": 2, "msg": "创建失败，请重试"})

    return JsonResponse({"code":1,"msg":"该相册已存在"})


def editAlbum(request):
    """
    编辑相册处理
    :param request:
    :return:
    """
    # 待编辑的相册的id
    album_id =request.POST.get("album_id")
    album_name = request.POST.get("album_name")  # 相册名称
    sort = request.POST.get("sort")  # 排序
    # 判断该相册是否存在
    exist_count = len(list(models.SysAlbum.objects.filter(album_name=album_name)))
    if exist_count == 0:
        try:
            models.SysAlbum.objects.filter(album_id=album_id).update(album_name=album_name,sort=sort)
            return JsonResponse({"code": 0, "msg": "编辑成功"})
        except:
            return JsonResponse({"code": 1, "msg": "编辑失败，请重试"})
    return JsonResponse({"code": 2, "msg": "该相册名称已存在"})


def delAlbum(request):
    """
    删除相册处理
    :param request:
    :return:
    """
    # 得到待删除的相册的id
    album_id =request.POST.get("album_id")
    try:
        models.SysAlbum.objects.filter(album_id=album_id).delete()
        return JsonResponse({"code": 0, "msg": "删除成功"})
    except:
        return JsonResponse({"code": 1, "msg": "删除失败"})


def albumPictureList(request):
    """
    相册图片管理
    :param request:
    :return:
    """
    # 先得到默认相册的album_id 如果url的album_id不规范则返回默认相册的图片数据
    album_id_default =models.SysAlbum.objects.filter(is_default=1).first().album_id
    album_id =request.GET.get("album_id",album_id_default)
    if request.POST.get("album_id"):
        album_id =request.POST.get("album_id")
    # 得到所有相册的id列表
    album_id_list =[i["album_id"] for i in models.SysAlbum.objects.values("album_id").all()]
    # 如果得到的album不存在则返回默认相册的图片数据
    if int(album_id) not in album_id_list:
        album_id =album_id_default

    # 获取该相册的数据
    album_name =models.SysAlbum.objects.filter(album_id=album_id).first().album_name
    # 获取该相册中的图片数据
    picture_list =list(models.SysAlbumPicture.objects.filter(album_id=album_id).values("pic_id","pic_name","pic_cover","pic_size","upload_time"))
    # 相册封面
    album_cover =picture_list[0].get("pic_cover") if len(picture_list)>0 else "http://xcx.bafelli.com/public/admin/images/album/album_cover_default.png"
    # 将上传时间进行格式转换
    for item in picture_list:
        item["upload_time"] =datetime.datetime.fromtimestamp(item["upload_time"]).strftime("%Y-%m-%d")
    # 分页处理
    paginator = Paginator(picture_list, 12)  # 分页器对象
    page_obj = paginator.page(1)  # 当前页的page对象

    # 整理出要返回的数据
    ret_data = {
        "album_id":album_id,
        "count": paginator.num_pages*10,  # 分页数据总数
        "album_name": album_name,
        "album_cover": album_cover,
        "pic_list":list(page_obj)
    }
    print(ret_data)

    # 浏览器发起的请求
    if request.method == "GET":
        return render(request,'goods/albumPictureList.html',context=ret_data)
    # 前台分页触发的ajax请求
    try:
        album_id_default = models.SysAlbum.objects.filter(is_default=1).first().album_id
        page = request.POST.get("page", 1)  # 页码
        page_obj = paginator.page(page)
        ret_data["code"] =0
        ret_data["pic_list"] =list(page_obj)
        return JsonResponse(ret_data)
    except:
        return JsonResponse({"code": 1, "msg": "error"})


def editAlbumPicture(request):
    """
    编辑相册图片
    :param request:
    :return:
    """
    pic_id =request.POST.get("pic_id") # 待编辑的图片id
    pic_name =request.POST.get("pic_name")  # 编辑后的图片名称
    try:
        models.SysAlbumPicture.objects.filter(pic_id=pic_id).update(pic_name=pic_name)
        return JsonResponse({"code": 0, "msg": "编辑成功"})
    except:
        return JsonResponse({"code": 1, "msg": "编辑失败，请重试"})


def delAlbumPicture(request):
    """
    删除相册图片
    :param request:
    :return:
    """
    pic_id =request.POST.get("pic_id") # 待删除的图片id
    pic_id_list =request.POST.getlist("pic_id_list")  # 待删除的图片id列表
    print('pic_id---',pic_id)
    print("pic_id_list---",pic_id_list)
    try:
        if pic_id:  # 删除一张
            models.SysAlbumPicture.objects.filter(pic_id=pic_id).delete()
        if len(pic_id_list) >0:  # 删除多张
            models.SysAlbumPicture.objects.filter(pic_id__in=pic_id_list).delete()
        return JsonResponse({"code": 0, "msg": "删除成功"})
    except:
        return JsonResponse({"code": 1, "msg": "删除失败"})


def test(request):
    """
    测试
    :param request:
    :return:
    """
    img_list =request.FILES.getlist("file")
  
    return JsonResponse({"msg":"success"})

