# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:48:24 2021

@author: Administrator
"""
# 文件目的是每隔一段时间爬微博热搜并存储在本地
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

hot_url = 'https://s.weibo.com/top/summary/'
# 热搜榜链接
folderPath = r'E:\python社区版\python项目\新建文件夹\Python网上项目代码\网上爬虫案例运行和调试\微博存储'
# 文件存储目录
if os.path.exists(folderPath):
    pass
else:
    os.mkdir(folderPath)
# 建立文件夹

columns = []
for i in range(50):
    columns.append('hot_text%s' % i)
    columns.append('hot_number%s' % i)
    # 建立存储DataFrame的列名，分别是热搜文本和热度

if __name__ == "__main__":
    pre_date = '20000101'
    # 初始化一个前一日期
    while 1:
        try:
            current_date = time.strftime("%Y%m%d", time.localtime())
            # 当前日期
            filePath = folderPath + '/%s.csv' % current_date
            # 文件存储位置
            if current_date == pre_date:
                pass
            else:
                today_data = pd.DataFrame(columns=columns)
                # 将今天所有的数据初始化一个DataFrame
            now_localtime = time.strftime("%H%M", time.localtime())
            # 现在时间，精确到分
            if int(now_localtime) % 5 == 0:
                # 每5分钟执行一次
                news = []
                # 新建数组临时存放热搜榜
                r = requests.get(hot_url)
                # 向链接发送get请求获得页面
                soup = BeautifulSoup(r.text, 'lxml')
                # 解析页面

                urls_titles = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
                hotness = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')
                # 获取文本和热度
                for i in range(len(urls_titles) - 1):
                    title = urls_titles[i + 1].get_text()
                    # get_text()获得a标签的文本
                    news.append(title)
                    hotness_number = hotness[i].get_text()
                    # 获得热度文本
                    news.append(hotness_number)
                    # 数据添加到临时存储数组中
                today_data.loc[now_localtime] = news
                # 将数组添加到DataFrame中
                if os.path.isfile(filePath):
                    os.remove(filePath)
                    # 删除原有文件
                else:
                    pass
                today_data.to_csv(filePath)
                # 写入硬盘
                time.sleep(200)
            else:
                time.sleep(20)
            pre_date = current_date
            # 改变前一日期
        except:
            time.sleep(5)
