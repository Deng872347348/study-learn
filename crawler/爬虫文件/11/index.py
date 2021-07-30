# encoding:utf-8
import requests
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import pandas as pd
from threading import Thread
from queue import Queue
"""
Python 版本：3.6
作者：宋哈哈
VX: 1436099893 , 外接爬虫单子

功能解释：

    if __name__ == '__main__': 功能：
        
        1.从网页直接手工复制了 make 的html代码 。用bs4 筛选出关键词。
        2.讲关键词存储到 key_list 队列中
        ====================================================
        对象程序 结束后：
        1.实列化 down_url 对象多线程爬取数据
        2.实列化 down_data 对象多线程爬取详细数据，并将数据添加到 list 中
        3.导出到 csv 中。
    
    class down_url 对象功能:
        1.导入关键词  key_list.get() 到 par 字典数据中。
    
        2.手工获取JSON文件URL，手工分析得到之后得到 url，par，endurl，三个关键信息，然后将这三个信息拼接，得到响应200d的URL。
    
            endurl 分析：
                1.iDisplayStart=100 ，经过手工测试后要等于 100 
                2.iDisplayLength=10000 ，这个是显示数据长度，也就是显示多少行。随意取个最大值，我取的是 1w 
                3.修改上面两个数据后就能在一个 URL 中获取所有的数据。
                
            par 分析：
                在 开发工具中的 Query String Parametes 得到：
            
            urlencode(par) 功能：
                主要用于把字典数据相加在一起。
            
        2.因为拼接在一起的会出现错误，源链接 是 22，拼接出来是 27 , 所以把拼接出来的URL进行replace替换
    
        3.后面就是正常的请求，判断请求是否成功，如果成功，则获取数据，然后把 获取的到 数据 存储到 jsondata_list 队列中
    
    
    class down_data 对象功能：
        1.讲 jsondata_list 存储的数据，导入到 down_data对象中
        2.用json 库，进行赛选出数据
        3.添加到 if __name__ == '__main__': 下新建的空列表中。
    


"""


key_list = Queue() #
jsondata_list = Queue()

class down_url(Thread):
    def __init__(self, key_list):
        Thread.__init__(self)
        self.url_queue = key_list # 要不要都无所谓
    def run(self):

        headers = { # headers 模拟浏览器

            'Cookie': '_ga=GA1.2.1676485634.1606510156; _gid=GA1.2.358511258.1606510156; intercom-id-ilj0t64m=610b3945-d748-42b7-a182-a4e3f758780f; ROUTEID=.2; _ga=GA1.3.1676485634.1606510156; _gid=GA1.3.358511258.1606510156; _gat_UA-148350090-1=1; _gat=1; _gat_gtag_UA_125951037_1=1; intercom-session-ilj0t64m=cGtPNmg4TVd1VnBpUnYwandIaEV5bFZIdnl0c0ovWC9GTkZUdDNFZTlIaDJLRGhra2xGL3dzN3k0eU54K2pFVy0tU3RJQkFGYlZSbmdmQ1lMVTNoeFpUQT09--5e2561f60e8324412660cbf829182007b226bb48; _myfitment_session=RVdZUDZwZDA1M2dzNzZ6UEVIbG4zUkJkZWlVRU5TTkRCWmRyaW44OHhXRkhXWDhGeFRrSCtjS3V1RUNXNkM5NlRmWWloWWVNZ1JuS01nOWRjZHFmVXVxZkxpWnpkUGM1VURFSzB3UXpHa3NBQTZWZkp3WUFvRjNIUGJVRjNrbUVZMWJPM0c2eG9qQVhuRVpIT2pjK0FBTjB3SWNOU0hIQ0Y3LzFwclFOak13RE9YcFJsSkJDMEliQlN1eTZ0cTRZM3NjTnhmL1plUFBtbDJmWlc0dGdIamVIOU9OQzRnYkN1VlhTOUp6NlhlSXZ2dnFpeU1ld281YXFEY01CM0JoUTdORmRNNjBMakI1RkhrYVU1WnBYMHg4cVhDb0s1OTZaaDdadVZDUkFXbDg9LS1JZVUyT0M4ZTEwVjZlZXIvNmQxb1NnPT0%3D--4c4efa363d801efc5882888ddc3c0f1bd3b4c69b',
            'Host': 'app.myfitment.com',
            'Referer': 'https://app.myfitment.com/apps/new',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'X-CSRF-Token': 'TB2ezP1L/38aRQdP0wM67y5+GBqfNOyOsGGSL2h69VRhOdKNQNhpHDj/HzJi3cjwX5wy6Q+rHUEwKDDhjvgEvQ==',
            'X-Requested-With': 'XMLHttpRequest'

        }

        url = 'https://app.myfitment.com/apps/search_vehicles.json?' # 头部url

        par = {
            "search_hash": {"standard_id": 6, "attribute1": ["", key_list.get()], "attribute2": [""], "attribute3": [""], # 局部url的 par
                            "selected_index": 1},
        }

        endurl = "&sEcho=2&iColumns=3&sColumns=%2C%2C&iDisplayStart=100&iDisplayLength=10000&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&_=1606654594514" # 尾部的 url

        urls = url + urlencode(par) + endurl # 拼接 头部 局部 尾部

        newurl = str("%s%s" % (urls, urlencode(par))).replace('27', '22') # 替换 27 为 22

        response = requests.get(newurl, headers=headers) # 请求newurl

        if response.status_code == 200: #判断是否请求成功
            jsondata_list.put(json.loads(response.content)) # 用 json 解析的内容，放入到 jsondata_list 队列中
            print(newurl)

class down_data(Thread):
    def __init__(self, jsondata_list): # 接收 jsondata_list 队列中的数据
        Thread.__init__(self)
        self.jsondata_list = jsondata_list
    def run(self):

        datas = jsondata_list.get()['aaData'] # 筛选 jsondata_list 的数据
        for d in datas:
            makes = d['0'] # 获取的 MAKE 值
            models = d['1'] # 获取的 ModelS 值
            years = d['2'] # 获取 Year 值
            MAKE_LIST.append(makes) #添加到 list中
            MODELS_LIST.append(models) #添加到 list中
            YEAR_LIST.append(years) #添加到 list中



if __name__ == '__main__':
    # mains()
    MAKE_LIST = [] # 创建新列表，用于导入到 csv 中
    MODELS_LIST = []
    YEAR_LIST = []

    # 下方是获取 手工复制的HTML代码中的关键词
    path = 'name.html'
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    html = BeautifulSoup(htmlhandle, 'lxml')
    option_info = html.find_all('option')

    newlist = []

    for option in option_info:
        make_data = option.text
        newlist.append(make_data)

    for nl in newlist:

        key_list.put(nl)  # 将关键词添加到 key_list 队列中

    down_url_list = [] # 多线程爬取信息 下方大概有 500 个线程
    for i in range(len(newlist)):
        du = down_url(key_list)
        down_url_list.append(du)
    for dul in down_url_list:
        dul.start()
    for dul in down_url_list:
        dul.join()

    down_data_list = []# 多线程爬取信息 下方大概有 500 个线程
    for i in range(len(newlist)):
        dd = down_data(jsondata_list)
        down_data_list.append(dd)
    for ddl in down_data_list:
        ddl.start()
    for ddl in down_data_list:
        ddl.join()



    #导入到 CSV 中

    excel_info = {'Make': MAKE_LIST, 'Model': MODELS_LIST, 'Year': YEAR_LIST}
    df = pd.DataFrame(excel_info, columns=['Make', 'Model', 'Year'])

    df.to_csv("myfitment.csv")
