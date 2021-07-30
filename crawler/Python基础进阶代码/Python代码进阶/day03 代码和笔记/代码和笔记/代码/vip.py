"""
方案：
    1. 直接破解并解析优酷VIP视频，切一小段一小短（VIP账户） - 账户封掉（很多人）
    2. 其他渠道找到面VIP视频，自己存储起来。
        https://v.youku.com/v_show/id_XNDk5MDM5Nzc1Mg==.html?spm=a2ha1.14919748_WEBMOVIE_JINGXUAN.drawer6.d_zj1_8&s=cdbf8fed71744bbca01f&scm=20140719.apircmd.4423.show_cdbf8fed71744bbca01f&s=cdbf8fed71744bbca01f
        拿着金刚川 -> 搜索
        自己的视频让你去下载（非常多）


1. 拷贝优酷VIP视频
2. 解析视频的 m3u8 格式 的地址（VIP账户、抓包、代理IP）
    https://jx.618g.com/?url=https://v.youku.com/v_show/id_XNDkyNzEwODQ2OA==.html?spm=a2ha1.14919748_WEBMOVIE_JINGXUAN.drawer6.d_zj1_5&s=4b5f7758321b11efbfbd&scm=20140719.apircmd.4423.show_4b5f7758321b11efbfbd
3. 获取到 m3u8 地址。
    并获取到视频的每一个ts文件获取到。
4. 分批下载ts文件（优酷对ts文件内容进行了加密）  AES加密->AES解密


自己电脑上：
    pip install requests
    pip install pycrypto
"""

import re
import os

import requests
from Crypto.Cipher import AES

# 优酷VIP视频地址
vip_video_url = "https://v.youku.com/v_show/id_XNDkyNzEwODQ2OA==.html?spm=a2ha1.14919748_WEBMOVIE_JINGXUAN.drawer6.d_zj1_5&s=4b5f7758321b11efbfbd&scm=20140719.apircmd.4423.show_4b5f7758321b11efbfbd"
# vip_video_url = "https://v.youku.com/v_show/id_XNTAzNDkxMDQ5Mg==.html?spm=a2ha1.14919748_WEBMOVIE_JINGXUAN.drawer6.d_zj1_7&s=03bca1240bd74fbda376&scm=20140719.apircmd.4423.show_03bca1240bd74fbda376&s=03bca1240bd74fbda376"


def run():
    # 1.根据视频地址解析m3u8地址
    res = requests.get(
        url="https://jx.618g.com/?url={}".format(vip_video_url)
    )
    match_object = re.search("url=(?P<url>.*\.m3u8)?", res.text)
    m3u8_url = match_object.groupdict().get("url")

    # 2.根
    res_suffix = requests.get(url=m3u8_url)
    suffix = res_suffix.text.splitlines()[-1]

    # 3.获取ts列表
    res_ts_list = requests.get(
        url="{}{}".format("https://v2.dious.cc", suffix)
    )

    # 获取秘钥
    key_url_match_object = re.search('URI="(?P<key>.*\.key)', res_ts_list.text)
    key_url = key_url_match_object.groupdict().get("key")
    res_key = requests.get(url=key_url)
    key = res_key.content
    print(key)  # b'facdf9bc99a9eca9'

    ts_list = re.findall('https.*\.ts', res_ts_list.text)
    print("ts共：{}".format(len(ts_list)))
    count = 0

    # 下载视频
    for ts_url in ts_list:
        res = requests.get(ts_url)
        file_name = ts_url.rsplit('/')[-1]

        # 视频解密
        cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
        result = cipher.decrypt(res.content)

        #
        data = result.split(b"|", 1)[-1]

        file_path = os.path.join('files', file_name)
        with open(file_path, mode='wb') as file_object:
            file_object.write(data)
        count += 1
        msg = "\r已下载：{}".format(count)
        print(msg, end='')
    print("\n下载成功")


if __name__ == '__main__':
    run()
