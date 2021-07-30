import requests
from lxml import etree
import os
import time

url = 'http://sc.chinaz.com/jianli/free.html'
if not os.path.exists('./moban'):
    os.mkdir('./moban')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


if __name__ == '__main__':
    while(1):
        print(url)
        response = requests.get(url,headers=headers)
        response.encoding ='utf-8'
        page_text = response.text
        datail_kf = etree.HTML(page_text)
        mo_list = datail_kf.xpath('//div[@class="bggray clearfix pt20"]/div[3]/div/div/div')

        for src in  mo_list:
            mo_url = src.xpath('./a/@href')[0]
            name = src.xpath('./a/img/@alt')[0]
            datail_text = requests.get('http:'+ mo_url,headers=headers).text
            tree = etree.HTML(datail_text)
            source = tree.xpath('//div[@class="bggray clearfix"]/div[2]/div[2]/div[1]/div[@class="down_wrap"]/div[2]//li/a/@href')[0]
            resourse = requests.get(source,headers=headers).content
            with open('./moban/'+name+'.rar','wb') as s:
                s.write(resourse)
            print(name)
            print(source)
            time.sleep(2)

        next_list = datail_text.xpath('//div[@class="bggray clearfix pt20"]/div[4]/div/a[@class="nextpage"]/@href')
        if next_list ==[]:break
        url = 'https://sc.chinaz.com/tag_jianli/' + next_list[0]
