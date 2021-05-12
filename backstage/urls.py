from django.urls import path,include
from . import views

"""
后台app的路由文件
"""

urlpatterns = [
    path('base/',views.baseTest) # 渲染模板
    ,path('login/',views.login) # 用户登录页面
    ,path('loginHandle/',views.loginHandle) # 管理员登录处理
    ,path('',views.index) # 后台首页
    ,path('upload/',views.upload) # 图片上传
    ,path('goods/goodslist/',views.goodslist) # 商品模块--商品列表页面
    ,path('goods/addgoods/',views.addgoods) # 商品模块--发布商品页面
    ,path('goods/goodscategory/',views.goodsCategory) # 商品模块--商品分类列表页面
    ,path('goods/addgoodscategory/',views.addGoodsCategory) # 商品模块--添加商品分类页面
    ,path('goods/goodsAttr/',views.goodsAttr) # 商品模块--商品属性
    ,path('goods/addgoodsAttr/',views.addgoodsAttr) # 商品模块--添加商品属性
    ,path('goods/goodsRecommend/',views.goodsRecommend) # 商品模块--商品推荐模块
    ,path('goods/goodsRecommend/list/',views.goodsRecomList) # 商品模块--商品推荐列表
    ,path('goods/goodsSpecList/',views.goodsSpecList) # 商品模块--商品规格
    ,path('goods/albumList/',views.albumList) # 商品模块--相册管理
    ,path('goods/addAlbum/',views.addAlbum) # --添加相册
    ,path('goods/editAlbum/',views.editAlbum) # --编辑相册
    ,path('goods/delAlbum/',views.delAlbum) # --删除相册
    ,path('goods/albumPictureList/',views.albumPictureList) # --相册图片管理
    ,path('goods/editAlbumPicture/',views.editAlbumPicture) # --相册图片编辑
    ,path('goods/delAlbumPicture/',views.delAlbumPicture) # --相册图片删除


]