import requests
import time
import json
import os
from pyquery import PyQuery as pq

def get_url():
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1676679984&containerid=1076031676679984&since_id=4635422224816960'
    headers = {
        'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212MobileSafari / 537.36',
        'X - Requested - With': 'XMLHttpRequest'
    }
    response = requests.get(url,headers=headers).json()
    return  response
#定义一个函数，解析数据
def parse_html(html):
    data=html['data']['cards']
    # print(data)
    weibo = {}
    for data1 in data:
        #定义一个列表
        weibo = {}
        mblog=data1["mblog"]
        weibo['内容']=pq(mblog["text"]).text()
        weibo["comments"]=mblog["comments_count"]
    print(weibo)
#定义个函数存储爬取到的数据

if __name__ == '__main__':
    html=get_url()
    res=parse_html(html)

