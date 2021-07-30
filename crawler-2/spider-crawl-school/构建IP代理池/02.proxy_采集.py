"""
项目需求：
代理ip抓取
1.需要获取数据的网站
2.网站的反爬手段
3.发送请求，获取响应
4.解析网页，获取数
5.运用IP
"""
import requests
from bs4 import BeautifulSoup
import random

# 解析网站  # 从ip代理网站获取ip列表
def get_ip_list(url,headers):
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.content,'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1,len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        # print(tds)
        ip_list.append(tds[1].text + ':' +tds[2].text) # 拼接成[ip:端口]的格式
        for i in  ip_list:
            with open('ip.txt', 'a') as  f:
               f.write(i)
    return ip_list

# 从列表里面中随机取出一个ip
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip) # 拼接成网址
    proxy_ip = random.choice(proxy_list)
    proxies = {'https':proxy_ip}

    return proxies


if __name__ == '__main__':

    # 1.需要获取数据的网站
    proxy_url = 'http://ip.yqie.com/proxygaoni/'

    # 2.网站的反爬手段
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    # 3.发送请求，获取响应
    response = requests.get(proxy_url,headers=headers)

    ip_list = get_ip_list(proxy_url,headers)
    proxies = get_random_ip(ip_list)


    print(proxies)

    # 4.解析网页，获取数
    # 5.运用IP