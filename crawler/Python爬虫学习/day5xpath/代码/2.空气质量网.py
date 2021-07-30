import requests
from  lxml import  etree
import os

if __name__ == '__main__':
    # url
    url = 'https://www.aqistudy.cn/historydata/'
    # headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    if not os.path.exists('./city'):
        os.mkdir('./city')

    # 发送请求
    f = open('./city/city.txt', 'w', encoding='utf-8')
    reponse = requests.get(url,headers=headers).text
    # print(reponse)
    tree = etree.HTML(reponse)
    # 数据解析
    normal_li_List = tree.xpath('//div[@class="container"]//div[@class="all"]/div[2]/ul/div[2]/li')

    for normal_li in normal_li_List:
        dateli = normal_li.xpath('./a/text()')
        print(dateli)
        #f.write(dateli[0] + '\n')
    # 保存文件


