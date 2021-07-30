from lxml import etree
import requests
import csv
def get_url():
    url='https://s.weibo.com/top/summary'
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
    }
    response=requests.get(url,headers).text
    html=etree.HTML(response)
    informat=html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td/a')
    filename = '关键字'
    filehref = '关键字链接'
    for a in informat:
        name=a.xpath('./text()')[0]
        href=a.xpath('./@href')[0]
        href_name='https:/'+href
        print(name)
        print(href_name)
        # print(href_name)
        # with open('weibo_1.txt','w',encoding='gb2312') as f:
        #     f.write(name+'\n'+href_name+'\n')
        with open('weibo.csv','a',encoding='UTF-8',newline='') as fp:
            writer=csv.writer(fp)
            header=["标题","链接"]
            writer.writerow([name,href_name])


if __name__ == '__main__':
    get_url()