import requests
from lxml import etree
import os
import time
def RequestInde():
        url='https://shaoyang.58.com/ershoufang/e2j4/?PGTID=0d200001-008f-fda5-c488-c73ff28dd8f8&ClickID=1'
        headers={
            'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36'
        }
        response=requests.get(url,headers=headers).text
        #print(response)
        return response
#数据的提取和解析
def dataEx(response):
    tree=etree.HTML(response)
    #print(tree)
    list_all=tree.xpath('//div[@class="property-content-detail"]')
    #print(list_all)
    for a in list_all:
        name=a.xpath('./div[@class="property-content-title"]/h3[@class="property-content-title-name"]/text()')[0]
        address=a.xpath('./section/div[@class="property-content-info property-content-info-comm"]/p/text()')[0]
        house_address=a.xpath('./section/div[@class="property-content-info property-content-info-comm"]/p/span/text()')
        house_address=address+','+house_address[0]+','+house_address[1]+','+house_address[2]
        # print(house_address)
        # print(name)
        with open('58.txt', 'a', encoding='utf-8') as f:
          f.write(name+'\n')
          f.write(address+','+house_address+'\n')
          print('下载完成')
if __name__ == '__main__':
    re=RequestInde()
    dataEx(re)

