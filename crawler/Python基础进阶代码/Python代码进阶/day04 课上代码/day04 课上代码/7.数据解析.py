#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    pip install requests
    pip install BeautifulSoup4
"""
import re
import requests
from bs4 import BeautifulSoup

# 想豆瓣发请求并获取内容
res = requests.get(
    url="https://www.douban.com/group/topic/79870081/",
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
)

# 提取邮箱
bs_object = BeautifulSoup(res.text, "lxml")
# <p class=" reply-content">1126402165@qq.com</p>
comment_object_list = bs_object.find_all("p", attrs={"class": "reply-content"})

count = 0
for comment_object in comment_object_list:
    text = comment_object.text
    regex_email = re.search("\w+@\w+.\w+", text, flags=re.A)  # 正则
    if not regex_email:
        continue
    count += 1
    print(regex_email.group())

print("总条数为：",count)