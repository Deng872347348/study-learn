# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

import time
import os
import random
from queue import Queue
from threading import Thread

url_queue = Queue() # 创建队列

carUrl_queue = Queue() # 创建队列

carImg_info = Queue()# 创建队列





class CyclingPhotos(Thread):
    """
    0.传入 切片出来的 URL

    1.然后多线程获取，将获取的URL，保存到 carUrl_queue 队列中

    """

    def __init__(self, url_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        # self.carUrl_queue = carUrl_queue

    def run(self):
        headers = {
            'COOKIE': 'PHPSESSID=648d1j9pk5f12gi1lilbpcttf8; _ga=GA1.2.1686595422.1606499697; _gid=GA1.2.287256998.1606499697',
            'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'Host': 'stock.fuelapi.com',
            'Referer': 'https://stock.fuelapi.com/vehicles/list?make_id=5&year=&model='
        }
        while self.url_queue.empty() == False:
            url = self.url_queue.get()  # 取到url
            print(url)
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    carUrl_queue.put(response.content)  # 将汽车首页的html 代码存储到 carUrl_queue
            except:
                with open('请求报错的首页URLS.txt','a+',encoding='utf-8') as f:
                    f.write(url+'\n')
                    f.close()
                    pass




class CarInfourl(Thread):
    """
    0.传入URL获取VIEW 的跳转链接。
    1.然后进行拼接，传到 carImg_info 队列中

    """
    def __init__(self, carUrl_queue):
        Thread.__init__(self)
        self.carUrl_queue = carUrl_queue

    def run(self):
        while self.carUrl_queue.empty() == False:


            html = BeautifulSoup(self.carUrl_queue.get(),'lxml')
            td = html.find_all('a', class_='view-products-button')
            # print(td)
            for t in td:
                ahref = t['href']
                view_url = "https://stock.fuelapi.com" + ahref
                carImg_info.put(view_url) # 将汽车首页的view的连接代码存储到 carImg_info


class Imgurl(Thread):
    """
    0.请求VIEW跳转后的页面的HTML，并用BS4筛选，判断。
    1.如果 1280 有图片就直接下载，如果没有就 用 640
    2.将 url 保存到 txt 文本中 ，切记之类就要分类，并把分类和文件名 写入 txt 中


    """

    def __init__(self, carImg_info):
        Thread.__init__(self)
        self.carImg_info = carImg_info
    def run(self):
        while self.carImg_info.empty() == False:
            print(self.carImg_info.get())
            headers = {
                'COOKIE': 'PHPSESSID=648d1j9pk5f12gi1lilbpcttf8; _ga=GA1.2.1686595422.1606499697; _gid=GA1.2.287256998.1606499697',
                'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                'Host': 'stock.fuelapi.com',
                'Referer': 'https://stock.fuelapi.com/vehicles/list?make_id=5&year=&model='
            }

            try:
                requ = requests.get(self.carImg_info.get(),headers=headers)
            except:
                with open('请求报错的汽车图片URLS.txt','a+',encoding='utf-8') as f:
                    f.write(self.carImg_info.get()+'\n')
                    f.close()
                    pass
            else:
                html = BeautifulSoup(requ.content, 'lxml')
                stills_white_1280 = html.find_all('div', id='stills_white_1280')
                car_name = html.find_all('div', id='list-header')

                if "No assets available in this format" in str(stills_white_1280): #判断 1280 有没有 图片，如果有继续执行。如果没有执行 else。
                    stills_0640 = html.find_all('div', id='stills_0640')
                    for s0640 in stills_0640:
                        s0640_a = s0640.find_all('a')
                        for x in s0640_a:
                            img_down_url0640 = x.text
                            print(img_down_url0640)

                            number = random.sample(range(1, 100000000000000), 1)[0]
                            new_number = random.sample(range(1000000, 1000000000000000), 1)[0] + number  # 图片名称

                            for c0640 in car_name:
                                file_name0640 = str(c0640.text).replace('	', '').replace('\n', '')  # 文件夹名
                                file_banks0640 = str(c0640.text).replace('	', '').replace('\n', '').split(' ')[1]  # 分类
                                file_path0640 = os.path.join(file_banks0640, file_name0640)
                                with open('car_img_down640S.txt', 'a+', encoding='utf-8') as f: #先将 url 和 要保存的PATH 写入到 文本中，暂时不下载，等待全部完成后，在读取 txt 多线程下载
                                    f.write("%s+%s+%s"%(img_down_url0640,file_path0640,new_number)+'\n')
                                    f.close()

                else:

                    for s1280 in stills_white_1280: # 有图片则继续爬取图片的URL
                        s1280_a = s1280.find_all('a')
                        for s in s1280_a:
                            img_down_url1280 = s.text
                            print(img_down_url1280)

                            number = random.sample(range(99, 100000000000000), 1)[0]
                            new_number = random.sample(range(100000000000000, 1000000000000000), 1)[0] + number  # 图片名称

                            for c in car_name:
                                file_name = str(c.text).replace('	', '').replace('\n', '')  # 文件夹名
                                file_banks = str(c.text).replace('	', '').replace('\n', '').split(' ')[1]  # 分类
                                file_path1280 = os.path.join(file_banks, file_name)

                                with open('car_img_down1280S.txt', 'a+', encoding='utf-8') as f:#先将 url 和 要保存的PATH 写入到 文本中，暂时不下载，等待全部完成后，在读取 txt 多线程下载
                                    f.write("%s+%s+%s" % (img_down_url1280, file_path1280, new_number)+'\n')
                                    f.close()

def mains():




    n = 1
    m = 2
    while range(n, m): # 切片式 获取 URL

        for i in range(n, m):
            url = "https://stock.fuelapi.com/vehicles/list/{}?make_id=&year=&model=".format(i)
            print(n, m)
            print(url)
            url_queue.put(url)

        # 50个线程爬取数据

        CyclingPhotos_list = []
        for i in range(50):
             cp = CyclingPhotos(url_queue)
             CyclingPhotos_list.append(cp)


        for cp in CyclingPhotos_list:
            cp.start()
        for cp in CyclingPhotos_list:
            cp.join()


        # 获取 汽车视图信息的url
        CarInfourl_list = []
        for i in range(50):
             cf = CarInfourl(carUrl_queue)
             CarInfourl_list.append(cf)


        for cf in CarInfourl_list:
            cf.start()
        for cf in CarInfourl_list:
            cf.join()

        #获取汽车图片的下载url

        Imgurl_list = []
        for i in range(50):
             il = Imgurl(carImg_info)
             Imgurl_list.append(il)


        for il in Imgurl_list:
            il.start()
        for il in Imgurl_list:
            il.join()

        # 判断循环，如果大于最大页码,退出 切片循环
        n += 1
        m += 1
        if m == 278:
            break




if __name__ == '__main__':
    mains()

