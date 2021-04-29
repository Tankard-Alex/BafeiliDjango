# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=100)
    album_cover = models.CharField(max_length=255)
    is_default = models.IntegerField()
    sort = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'album'


class AlbumPicture(models.Model):
    pic_id = models.AutoField(primary_key=True)
    album_id = models.IntegerField()
    pic_name = models.CharField(max_length=100)
    pic_path = models.CharField(max_length=255)
    pic_spec = models.CharField(max_length=100)
    upload_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'album_picture'


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num = models.SmallIntegerField()
    uid = models.IntegerField()
    goods_picture = models.IntegerField()
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.IntegerField()
    size = models.IntegerField()
    stock = models.IntegerField(blank=True, null=True)
    thumb = models.CharField(max_length=255)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Collection(models.Model):
    uid = models.IntegerField()
    goodsid = models.IntegerField(db_column='goodsId')  # Field name made lowercase.
    createtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collection'


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_type_id = models.IntegerField()
    coupon_name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    at_least = models.DecimalField(max_digits=10, decimal_places=2)
    range_type = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.CharField(max_length=20)
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon'


class CouponDetails(models.Model):
    coupon_id = models.IntegerField()
    coupon_type_id = models.IntegerField()
    uid = models.IntegerField()
    use_order_id = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    fetch_time = models.IntegerField(blank=True, null=True)
    use_time = models.IntegerField()
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_details'


class CouponGoods(models.Model):
    coupon_id = models.IntegerField()
    goods_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'coupon_goods'


class CouponType(models.Model):
    coupon_type_id = models.AutoField(primary_key=True)
    coupon_type_name = models.CharField(max_length=255)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_type'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=100)
    category_id_1 = models.IntegerField()
    category_id_2 = models.IntegerField()
    market_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()
    min_stock_alarm = models.IntegerField(blank=True, null=True)
    sell_count = models.IntegerField(blank=True, null=True)
    collection_count = models.IntegerField(blank=True, null=True)
    picture = models.IntegerField()
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    goods_spec = models.TextField()
    goods_attribute = models.TextField(blank=True, null=True)
    putaway_time = models.IntegerField(blank=True, null=True)
    soldout_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    ifsale = models.IntegerField(blank=True, null=True)
    colorimgs = models.TextField(blank=True, null=True)
    newsattrid = models.CharField(db_column='newsAttrId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modellingattrid = models.CharField(db_column='modellingAttrId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goods_attrlist = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255)
    sale = models.IntegerField(blank=True, null=True)
    goodsinfo = models.CharField(db_column='goodsInfo', max_length=255)  # Field name made lowercase.
    capacity = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsAttribute(models.Model):
    attr_id = models.AutoField(primary_key=True)
    attr_name = models.CharField(max_length=255)
    in_use = models.IntegerField()
    create_time = models.IntegerField()
    modify_time = models.IntegerField(blank=True, null=True)
    cate_id = models.IntegerField()
    is_visible = models.IntegerField()
    pid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goods_attribute'


class GoodsCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    pid = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    is_visible = models.IntegerField()
    attr_id = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    category_pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsRecommend(models.Model):
    recommend_name = models.CharField(max_length=50)
    goods_id = models.CharField(max_length=255, blank=True, null=True)
    if_view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goods_recommend'


class GoodsSpec(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=255)
    show_type = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    spec_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_spec'


class GoodsSpecValue(models.Model):
    spec_value_id = models.AutoField(primary_key=True)
    spec_id = models.IntegerField()
    spec_value_name = models.CharField(max_length=100)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goods_spec_value'


class Member(models.Model):
    uid = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=50)
    member_level = models.IntegerField()
    reg_time = models.IntegerField()
    redpacket = models.FloatField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'


class MemberAccount(models.Model):
    uid = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    member_consume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdraw = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_account'


class MemberBalanceWithdraw(models.Model):
    withdraw_no = models.CharField(max_length=100, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    realname = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    ask_for_date = models.IntegerField(blank=True, null=True)
    paymentint_date = models.IntegerField(blank=True, null=True)
    modify_date = models.IntegerField(blank=True, null=True)
    transfer_type = models.IntegerField(blank=True, null=True)
    transfer_name = models.CharField(max_length=50, blank=True, null=True)
    transfer_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transfer_status = models.IntegerField(blank=True, null=True)
    transfer_remark = models.CharField(max_length=255, blank=True, null=True)
    transfer_result = models.CharField(max_length=255, blank=True, null=True)
    transfer_no = models.CharField(max_length=255, blank=True, null=True)
    transfer_account_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_balance_withdraw'


class MemberLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=50)
    goods_discount = models.DecimalField(max_digits=3, decimal_places=2)
    desc = models.CharField(max_length=1000, blank=True, null=True)
    is_default = models.IntegerField()
    quota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    effective = models.IntegerField(blank=True, null=True)
    redpacket = models.DecimalField(max_digits=10, decimal_places=2)
    express = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'member_level'


class Message(models.Model):
    uid = models.IntegerField()
    from_type_id = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    createtime = models.IntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message'


class MessageTemplate(models.Model):
    t_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    from_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_template'


class MktActivities(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000, blank=True, null=True)
    picture = models.CharField(max_length=255)
    goodsidlist = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    create_time = models.IntegerField()
    modify_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mkt_activities'


class MktHome(models.Model):
    recommended_name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    sort = models.IntegerField()
    ifview = models.IntegerField()
    goodsidlist = models.CharField(max_length=255, blank=True, null=True)
    pic_size = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkt_home'


class MktModelling(models.Model):
    modellingname = models.CharField(db_column='modellingName', max_length=50)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=255)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='linkType')  # Field name made lowercase.
    sort = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    ifview = models.IntegerField()
    pic_size = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkt_modelling'


class MktNav(models.Model):
    nav_id = models.AutoField(primary_key=True)
    nav_name = models.CharField(max_length=255)
    sort = models.IntegerField()
    create_time = models.IntegerField()
    modify_time = models.IntegerField(blank=True, null=True)
    if_show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mkt_nav'


class MktNewsCate(models.Model):
    newscatename = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255)
    sort = models.IntegerField()
    ifview = models.IntegerField()
    goodsidlist = models.CharField(max_length=255, blank=True, null=True)
    pic_size = models.CharField(max_length=100, blank=True, null=True)
    bigfocus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mkt_news_cate'


class MktNewsSmallCarousel(models.Model):
    img = models.CharField(max_length=255)
    goods_id = models.IntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mkt_news_small_carousel'


class MktNursing(models.Model):
    nursingname = models.CharField(db_column='nursingName', max_length=50)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=255)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='linkType')  # Field name made lowercase.
    sort = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    ifview = models.IntegerField()
    pic_size = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkt_nursing'


class MktRecommend(models.Model):
    recommended_name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    sort = models.IntegerField()
    ifview = models.IntegerField()
    goodsidlist = models.CharField(max_length=255, blank=True, null=True)
    pic_size_pic_size = models.CharField(db_column='pic_size\r\npic_size', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'mkt_recommend'


class MktSale(models.Model):
    sale_name = models.CharField(max_length=255)
    sale_rate = models.DecimalField(max_digits=2, decimal_places=1)
    img = models.CharField(max_length=255)
    sort = models.IntegerField()
    ifview = models.IntegerField()
    goodsidlist = models.CharField(max_length=255, blank=True, null=True)
    pic_size = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkt_sale'


class Order(models.Model):
    order_no = models.CharField(max_length=255)
    payment_type = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField()
    username = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    point = models.IntegerField(blank=True, null=True)
    coupon_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    user_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_company_id = models.IntegerField(blank=True, null=True)
    give_point_type = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    pay_time = models.IntegerField(blank=True, null=True)
    consign_time = models.IntegerField(blank=True, null=True)
    sign_time = models.IntegerField(blank=True, null=True)
    finish_time = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    refund_balance_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_status = models.IntegerField(blank=True, null=True)
    refund_type = models.CharField(max_length=255, blank=True, null=True)
    refund_reason = models.CharField(max_length=255, blank=True, null=True)
    refund_shipping_code = models.CharField(max_length=255, blank=True, null=True)
    refund_shipping_company = models.CharField(max_length=255, blank=True, null=True)
    refund_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    address_id = models.IntegerField()
    vip_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    express = models.CharField(max_length=255, blank=True, null=True)
    express_id = models.CharField(max_length=255, blank=True, null=True)
    exchange = models.CharField(max_length=11, blank=True, null=True)
    info = models.CharField(max_length=1000, blank=True, null=True)
    goodsinfo_list = models.CharField(db_column='goodsInfo_list', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class OrderStatus(models.Model):
    state_id = models.AutoField(primary_key=True)
    order_statename = models.CharField(db_column='order_stateName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_status'


class RetailStore(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city_id = models.IntegerField()
    province_id = models.IntegerField()
    district_id = models.IntegerField()
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField()
    open_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retail_store'


class SysAlbum(models.Model):
    album_id = models.AutoField(primary_key=True)
    shop_id = models.IntegerField()
    pid = models.IntegerField()
    album_name = models.CharField(max_length=100)
    album_cover = models.CharField(max_length=255)
    is_default = models.PositiveIntegerField()
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_album'


class SysAlbumPicture(models.Model):
    pic_id = models.AutoField(primary_key=True)
    shop_id = models.PositiveIntegerField(blank=True, null=True)
    album_id = models.PositiveIntegerField()
    is_wide = models.IntegerField()
    pic_name = models.CharField(max_length=100)
    pic_tag = models.CharField(max_length=255)
    pic_cover = models.CharField(max_length=255)
    pic_size = models.CharField(max_length=255)
    pic_spec = models.CharField(max_length=100)
    pic_cover_big = models.CharField(max_length=255)
    pic_size_big = models.CharField(max_length=255)
    pic_spec_big = models.CharField(max_length=100)
    pic_cover_mid = models.CharField(max_length=255)
    pic_size_mid = models.CharField(max_length=255)
    pic_spec_mid = models.CharField(max_length=100)
    pic_cover_small = models.CharField(max_length=255)
    pic_size_small = models.CharField(max_length=255)
    pic_spec_small = models.CharField(max_length=255)
    pic_cover_micro = models.CharField(max_length=255)
    pic_size_micro = models.CharField(max_length=255)
    pic_spec_micro = models.CharField(max_length=255)
    upload_time = models.IntegerField(blank=True, null=True)
    upload_type = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    bucket = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_album_picture'


class SysArea(models.Model):
    area_id = models.AutoField(primary_key=True)
    rea_name = models.CharField(max_length=10)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_area'


class SysCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    province_id = models.IntegerField()
    city_name = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_city'


class SysCityEn(models.Model):
    city_id = models.AutoField(primary_key=True)
    province_id = models.IntegerField()
    city_name = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6)
    sort = models.IntegerField()
    city_zh = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_city_en'


class SysDistrict(models.Model):
    district_id = models.AutoField(primary_key=True)
    city_id = models.IntegerField()
    district_name = models.CharField(max_length=255)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_district'


class SysDistrictEn(models.Model):
    district_id = models.AutoField(primary_key=True)
    city_id = models.IntegerField()
    district_name = models.CharField(max_length=255)
    sort = models.IntegerField(blank=True, null=True)
    district_zh = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_district_en'


class SysProvince(models.Model):
    province_id = models.AutoField(primary_key=True)
    area_id = models.IntegerField()
    province_name = models.CharField(max_length=10)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_province'


class SysProvinceEn(models.Model):
    province_id = models.AutoField(primary_key=True)
    area_id = models.IntegerField()
    province_name = models.CharField(max_length=100)
    sort = models.IntegerField()
    province_zh = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_province_en'


class SysSettings(models.Model):
    set_id = models.AutoField(primary_key=True)
    web_name = models.CharField(max_length=50)
    commissionrate = models.IntegerField()
    service_weixin = models.CharField(max_length=50)
    vip_rules = models.TextField()
    integral_rules = models.TextField()
    commission_rules = models.TextField()

    class Meta:
        managed = False
        db_table = 'sys_settings'


class SysUser(models.Model):
    uid = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=255, blank=True, null=True)
    user_status = models.IntegerField()
    is_system = models.IntegerField()
    user_tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    wx_openid = models.CharField(max_length=255, blank=True, null=True)
    wx_info = models.CharField(max_length=1000, blank=True, null=True)
    current_login_ip = models.CharField(max_length=255, blank=True, null=True)
    last_login_ip = models.CharField(max_length=255, blank=True, null=True)
    reg_time = models.IntegerField()
    current_login_time = models.IntegerField(blank=True, null=True)
    last_login_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserAdmin(models.Model):
    uid = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    group_id_array = models.IntegerField(blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    admin_status = models.IntegerField()
    desc = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_admin'


class SysUserGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50)
    is_system = models.IntegerField(blank=True, null=True)
    module_id_array = models.CharField(max_length=1000, blank=True, null=True)
    desc = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modify_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_group'


class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    receiverprovince = models.CharField(db_column='receiverProvince', max_length=255)  # Field name made lowercase.
    receivercity = models.CharField(db_column='receiverCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    receiverdistrict = models.CharField(db_column='receiverDistrict', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    areaname = models.CharField(db_column='areaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='isDefault')  # Field name made lowercase.
    consignee = models.CharField(max_length=50)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_address'
