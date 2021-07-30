# encoding:utf-8
import requests
import pandas as pd
import os
import random
# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import time
import os
import random
from queue import Queue
from threading import Thread

read_info = pd.read_csv('car_img_url.csv',low_memory=False)
df_info = pd.DataFrame(read_info)

downurl = df_info['downurl']
filapath = df_info['filepath']
filename = df_info['filename']

read_info = pd.read_csv('car_img_url.csv', low_memory=False)
df_info = pd.DataFrame(read_info)
car_url_list = Queue()

class Url(Thread):
    """
    读取 csv 文件，是通过下载后得到 txt 文件转换的。


    """



    def __init__(self):
        Thread.__init__(self)
        # self.url_queue = url_list
    def run(self):

        downurl = df_info['downurl']

        downurl_list = downurl.values.tolist()[0:100000]
        for fp in downurl_list:
            # print("下载：", fp)
            car_url_list.put(fp)


class Downurl(Thread):
    """
    下载文件

    """


    def __init__(self, car_url_list):
        Thread.__init__(self)
        self.car_url_list = car_url_list

    def run(self):
        newpd = df_info[str(car_url_list.get()) == downurl]
        img_down_path = newpd['filepath'].values[0]  # 下载本地路径

        number = random.sample(range(1, 100000000000000), 1)[0]
        img_name = random.sample(range(1000000, 1000000000000000), 1)[0] + number  # 图片名称

        if os.path.isdir(img_down_path):
            try:
                requ = requests.get(car_url_list.get())
            except:
                with open("未下载连接.txt",'a+',encoding='utf-8') as k:
                    k.write(car_url_list.get())
                    k.close()
            else:
                print("下载：", car_url_list.get())
                with open("%s/%s.jpg" % (img_down_path, img_name), 'wb') as m:
                    m.write(requ.content)
                    m.close()
        else:
            try:
                os.makedirs(img_down_path)
            except:
                pass



if __name__ == '__main__':

    url_list = []

    for i in range(100):
        u = Url()
        url_list.append(u)
    for ul in url_list:
        ul.start()
    for ul in url_list:
        ul.join()

    Downurl_list = []

    for i in range(100):
        du = Downurl(car_url_list)
        Downurl_list.append(du)
    for dl in  Downurl_list:
        dl.start()
    for dl in  Downurl_list:
        dl.join()




