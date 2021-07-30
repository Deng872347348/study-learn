#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}

res = requests.get(
    url="https://www.douban.com/group/topic/79870081/",
    headers=HEADERS
)
bs_object = BeautifulSoup(res.text, "lxml")
url_list = []
paginator_object = bs_object.find("div", attrs={"class": "paginator"})
for a_ele in paginator_object.find_all("a"):
    url_list.append(a_ele.attrs.get("href"))

bs_object_list = [bs_object, ]
for url in url_list:
    response = requests.get(
        url=url,
        headers=HEADERS
    )
    page_bs_object = BeautifulSoup(response.text, "lxml")
    bs_object_list.append(page_bs_object)

count = 0
for bs_object_item in bs_object_list:
    comment_object_list = bs_object_item.find_all("p", attrs={"class": "reply-content"})
    for comment_object in comment_object_list:
        text = comment_object.text
        regex_email = re.search("\w+@\w+.\w+", text, flags=re.A)
        if not regex_email:
            continue
        count += 1
        print(regex_email.group())

print("获取邮箱的总数为：", count)
