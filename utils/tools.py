import os
import time
import oss2
from BafeiliPro import settings
from PIL import Image
import django
if django.VERSION >= (1, 7): # 自动判断版本
    django.setup()


def uploadOss(file_obj):
    """
    将文件上传至oss并返回访问地址
    :param file_obj: 类文件对象
    :return: 上传成功：访问地址  上传失败：None
    """
    raw_name = file_obj.name  # 拿到原文件名
    # 将文件名修改为时间戳的形式防止重复写入
    file_name = str(int(time.time() * 1000)) + "." + raw_name.split(".")[1]
    file_path = "static/admin/imgs/"
    write_name = file_path + file_name  # 文件存储的本地路径
    with open(write_name, 'wb') as f:
        for line in file_obj.chunks():
            f.write(line)

    auth = oss2.Auth(settings.OSSAccessKeyID, settings.OSSAccessKeySecret)
    # 创建bucket对象
    bucket = oss2.Bucket(auth, settings.OSSEndpoint, settings.OSSBucket)
    # Bucket 域名
    oss_domin = settings.OSSDomain
    # oss写入路径
    oss_path = "imgs/" + file_name
    result = bucket.put_object_from_file(oss_path, write_name)
    # print(result)
    # print(result.status)
    # 得到图片宽高信息
    fp =open(write_name, 'rb')
    im = Image.open(fp)
    fp.close()
    if result.status == 200:
        img_src = oss_domin + "/" + oss_path  # oss图片地址
        # print("图片上传成功")
        # print("所上传图片的地址为: %s" % img_src)

        # 将本地文件删除
        if os.path.exists(write_name):
            os.remove(write_name)
        # 将图片信息返回
        return {
            "pic_name":raw_name,
            "pic_size":str(im.size[0]) + "," +str(im.size[1]),
            "img_src":img_src
        }
    return None