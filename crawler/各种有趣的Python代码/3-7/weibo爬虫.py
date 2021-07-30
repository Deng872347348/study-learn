from fake_useragent import UserAgent  # 反爬虫请求头
import random
import requests
from bs4 import BeautifulSoup
import schedule
from datetime import datetime  # 处理时间
import time
import csv  # 数据存储


def main():
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    headers = {
        # 生成随机反爬虫请求头
        'User-Agent': str(UserAgent().random)
    }

    response = requests.get(url, headers=headers).text
    top_search_dict = {}  # 空字典，保存提取的数据
    soup = BeautifulSoup(response, 'html.parser')  # 创建解析对象

    items = soup.find_all('td', class_='td-02')  # 获取微博热搜数据
    for item in items:
        title = item.find('a').text.strip()  # 获取标题
        print(title)
        counts = item.find_all('span')
        print(counts)
    for i in counts:
    # 存储进入上方的空字典， 标准 键 数值 值
        top_search_dict[title] = i.get_text()
        top_search_dict['date'] = datetime.now().strftime('Y%/%m/%d %H:%M')  # 获取时间
            # 文件名称
        with open('weibo_search.csv', 'a', encoding='gbk', newline='') as f:  # 存储道csv
            w = csv.DictWriter(f, top_search_dict.keys())
            w.writeheader()
            w.writerow(top_search_dict)
main()
#
# def auto_spider(stop_time):
#     schedule.every(1).minutes.do(main)  # 设置每分钟进行一次调度
#     print("执行中")
#     while True:
#         if datetime.now().strftime('%H:%M') <= stop_time:  # 设置时间点判断执行调度时长
#             schedule.run_pending()  # 执行所有调度
#             time.sleep(60)
#         else:
#             break
#
#
# if __name__ == '__main__':
#     auto_spider(stop_time='19:47')
