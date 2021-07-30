from  lxml import  etree
import requests

def RequetesIndex():
    url = 'https://cs.58.com/chuzu/?PGTID=0d100000-0019-e00e-e45b-253ba491f069&ClickID=2'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response = requests.get(url,headers=headers).text
    # print(response.text)
    return response

def dataEx(response):
    tree = etree.HTML(response)
    li_lsit = tree.xpath('//ul[@class="house-list"]/li[@class="house-cell"]')
    fp = open('58.txt','w',encoding='utf-8')

    ll = len(li_lsit)
    for i in li_lsit:
        print(i.xpath('./div[@class="des"]/h2/a/text()')[0])
        fp.write((i.xpath('./div[@class="des"]/h2/a/text()')[0] + '\n'))

if __name__ == '__main__':
    re = RequetesIndex()
    dataEx(re)