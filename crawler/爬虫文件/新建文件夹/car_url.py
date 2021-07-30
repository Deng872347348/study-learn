# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

import time
import os
import random
from queue import Queue
from threading import Thread

url_list = Queue()

urllen = []



def car_models_id():

        url = 'https://stock.fuelapi.com/vehicles/list?make_id=&year='
        requ = requests.get(url)
        html = BeautifulSoup(requ.content, 'lxml')
        make_id = html.find_all('select', id='make-select')
        for make in make_id:
            option_value = make.find_all("option")
            for option in option_value:

                make_ids = str(option['value'])
                if make_ids.isdigit() == True:
                    if make_ids != "64":


                        web_url = "https://stock.fuelapi.com/vehicles/list?make_id={}&year=".format(make_ids)

                        with open("car_url.txt", 'a+', encoding='utf-8')  as f:
                            f.write(web_url + '\n')
                            f.close()



def page_url():
    with open("car_url.txt", 'r', encoding='utf-8') as r:
        file_url = r.read()
        new_file_url = str(file_url).split('\n')
        for nfu in new_file_url:
            if nfu != "":
                print(nfu)
                for i in range(1, 50):
                    page_number = str(nfu).replace("list?", 'list/{}?'.format(i))
                    # print(page_number)
                    with open("page_url.txt", 'a', encoding='utf-8') as f:
                        f.write(page_number + "\n")
                        f.close()


def judge():
    headers = {

        'Cookie': '_ga=GA1.2.1052782292.1606491477; _gid=GA1.2.1822982860.1606491477; PHPSESSID=h1piacf942hmo4hhod8etvtq24',
        'Host': 'stock.fuelapi.com',
        'Referer': 'https://stock.fuelapi.com/vehicles/list/1?make_id=5&year=',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

    }

    url_list = []
    page_number = []
    with open("car_url.txt", 'r', encoding='utf-8') as r:
        file_url = r.read()
        new_file_url = str(file_url).split('\n')
        for nfu in new_file_url:
            if nfu != "":

                requ = requests.get(nfu, headers=headers)
                html = BeautifulSoup(requ.content, 'lxml')
                page_div = html.find_all('div', class_='pagination')
                if page_div == []:
                    page_num = "1"
                    with open("CAR_URL_PAGE.txt", 'a+', encoding='utf-8') as f:
                        f.write("%s,%s\n" % (nfu, page_num))
                        f.close()
                else:
                    number_list = []
                    for pd in page_div:
                        ul = pd.find_all('li')
                        for u in ul:
                            page_number = u.text
                            if page_number.isdigit() == True:
                                number_list.append(page_number)
                    print(number_list)
                    maxnumber = number_list[-1]
                    print(maxnumber)

                    with open("CAR_URL_PAGE.txt", 'a+', encoding='utf-8') as f:
                        f.write("%s,%s\n" % (nfu, maxnumber))
                        f.close()

                print(nfu)


def read_page_url():
    page_url = []
    page_number = []
    with open("CAR_URL_PAGE.txt", 'r', encoding='utf-8') as r:

        file_url = r.read()
        new_file_url = str(file_url).split('\n')
        for nfu in new_file_url:
            if nfu != "":
                # print(nfu)
                new_nfu = str(nfu).split(',')
                for i in range(1,int(new_nfu[1])+1):
                    print(i)
                    new_page = str(new_nfu[0]).replace("list?", 'list/{}?'.format(i))
                    # with open("new_page_url.txt", 'a+', encoding='utf-8') as f:
                    #         f.write(new_page + "\n")
                    #         f.close()



def make_view():
    page_info = []
    with open("new_page_url.txt", 'r', encoding='utf-8') as r:

        file_url = r.read()
        new_file_url = str(file_url).split('\n')
        for nfu in new_file_url:
            if nfu != "":

                page_info.append(nfu)

    n = 0
    m = 2
    while True:
        page_list_slice = page_info[n:m]

        for pg in page_list_slice:
            # print(pg)
            print(pg)
            url_list.put(pg)
            # with open("iii.txt",'a+',encoding='utf-8') as  d:
            #     d.write("%s\n"%(pg))
            #     d.close()

        ul_list = []
        for i in range(len(page_list_slice)):
            print("正在 %s 线程运行程序" % len(page_list_slice))
            ul = url200(url_list)
            ul_list.append(ul)
        for u in ul_list:
            u.start()
        for u in ul_list:
            u.join()


        print(n, m)
        n=m
        m+=2
        if n>len(page_info):
            break


class url200(Thread):
    def __init__(self, url_list):
        Thread.__init__(self)
        self.url_list = url_list

    def run(self):

        while self.url_list.empty() == False:
            headers = {

                'Cookie': '_ga=GA1.2.1052782292.1606491477; _gid=GA1.2.1822982860.1606491477; PHPSESSID=h1piacf942hmo4hhod8etvtq24',
                'Host': 'stock.fuelapi.com',
                'Referer': 'https://stock.fuelapi.com/vehicles/list/1?make_id=5&year=',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

            }

            try:
                requ = requests.get(url_list.get(), headers=headers, timeout=60)
                html = BeautifulSoup(requ.content, 'lxml')

                view = html.find_all('td', class_='actions')
                for v in view:
                    View_text = v.find_all('a')[0].text
                    ahref = v.find_all('a')[0]['href']

                    if "View" == View_text:
                        home_url = 'https://stock.fuelapi.com'
                        view_url = home_url + ahref
                        print(view_url)
                        with open("VIEW请求URL.txt", 'a+', encoding='utf-8') as f:
                            f.write(view_url + '\n')
                            f.close()

            except:
                with open("VIEW请求报错URL.txt", 'a+', encoding='utf-8') as f:
                    f.write(url_list.get() + "\n")
                    f.close()


if __name__ == '__main__':
    make_view()
