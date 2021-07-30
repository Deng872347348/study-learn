import  requests

from lxml import etree

def RequestInde():
    url='https://www.aqistudy.cn/historydata/'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response=requests.get(url,headers=headers).text
    return  response
def dataEx(response):
    tree=etree.HTML(response)
    list=tree.xpath('//div[@class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]')
    for a in list:
        name=a.xpath('./div[@class="hot"]/div[@class="top"]/text()')[0]
        name_1=a.xpath('./div[@class="hot"]/div[@class="bottom"]/ul/li/a/text()')
        name_1=' '.join(name_1)
        # print(name)
        # print(name_1)
        hot_city=a.xpath('./div[@class="all"]/div[@class="top"]/text()')[0]
        all_city=a.xpath('./div[@class="all"]/div[@class="bottom"]/ul[@class="unstyled"]/div/li/a/text()')
        all_city='\n'.join(all_city)
        # print(hot_city)
        # print(all_city)
        with open('空气质量的城市.txt','a',encoding='utf-8') as f:
            f.write(name+'\n'+name_1+'\n'+hot_city+'\n'+all_city)
            print('下载成功')
if __name__ == '__main__':
    data=RequestInde()
    dataEx(data)