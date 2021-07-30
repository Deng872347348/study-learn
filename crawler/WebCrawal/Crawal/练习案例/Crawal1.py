# 导入数据架包
import os
import re

import requests

if __name__:
    # 创建一个文件夹，将图片存在里面
    if not os.path.exists('./Dengbo'):
        os.mkdir('./DengLibs')
    url = "https://www.bilibili.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
#
#<div class="zhuanji-inner-box zhuanji-img" style="background:url(.*?);"><\/div>
ex = '<div class="zhuanji-inner-box zhuanji-img" style="background:url(.*?);"><\/div>'
img_src_lisy = re.findall(ex, page_text, re.S)
# 拼接图片的地址
for src in img_src_lisy:
    src = 'http:' + src
    # 请求图片的二进制的数据
    img_data = requests.get(url=url, headers=headers).content
    # 生成图片的名称
    img_name = src.split('/')[-1]
    # 生成图片的一个路径
    imgPath = './DengLibs' + img_name
    # 数据的持久化
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功!!!')

