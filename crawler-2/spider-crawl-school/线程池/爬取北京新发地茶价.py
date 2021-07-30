#先提取单页面的数据
#上线程池，多个页面同时抓取
import  requests
from lxml import etree
import csv
from concurrent.futures import  ThreadPoolExecutor,ProcessPoolExecutor
f=open('data.csv',mode='w',encoding='utf-8')
csvwriter=csv.writer(f)
def download_one_page(url):
    resp=requests.get(url)
    resp.encoding=resp.apparent_encoding
    print(resp.text)
    #使用xpath对网页源代码进行解析和数据提取
    html=etree.HTML(resp.text)
    table=html.xpath("")
    trs=table.xpath("./tr")
    # print(len(trs))
    #拿到每个tr
    for tr in trs:
        txt=tr.xpath("")
        #对数据做简单的出来:\\ /去掉
        txt=(item.replace('\\','').replace('/','') for item in txt)
        #把数据存放到王杰中
        csvwriter.writerows(txt)
        print(url,"提取完毕")
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            #把下载任务提交给线程池
            t.submit(download_one_page(),f'')
    # 等带线程池中的任务全部执行完毕，才继续执行(守护)
    print('全部下载完成')