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
    ,path('goodslist/',views.goodslist) # 商品模块--商品列表页面
]