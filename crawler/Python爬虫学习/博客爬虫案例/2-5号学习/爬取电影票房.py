import requests
from  bs4 import BeautifulSoup
from lxml import etree
def get_request():
    #通过requests请求到电影票房的网页
    url='https://www.endata.com.cn/BoxOffice/index.html'
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.150Safari / 537.36'
    }
    text=requests.get(url,headers=headers)
    text.encoding='UTF-8'
    text=text.text
    #print(text)
    #使用BeautifulSoup进行解析
    soup=BeautifulSoup(text,'lxml')#后面这个是html的解析器
    tree=etree.HTML(text)
    #找到table
    table=soup.find('div',class_="ml20")
    #print(table)
    alist=tree.xpath('//div[@id="TopList"]//text()')
    print(alist)
    print(tree.xpath('//h6/span/text()'))
    for a in alist:
        print(a.xpath('./text()'))
    #找到table
    #find找到是一个标签
    #find_all找到一堆标签
    # f=open("电影票房.csv",mode='w')

    # trs=table.find_all("tr")
    # for tr in trs:#拿到每一个tr
    #
    #    lst=tr.find_all("id")#找到每一个id
    #    if len(lst)!=0:
    #        for td in lst:#拿到每一个id
    #             #print(td.text)#拿到td标签中的文本信息，就是我们要的电影信息
    #             with open('电影票房.csv','w') as f:
    #                  f.write(td.text.strip())#strip()默认去掉左右两端的空白(空格，换行符，制表符)
    #                  f.write(",")
    #                  f.write("\n")
if __name__ == '__main__':
    #for year in range(2000, 2020):  # 顾头不顾尾
        get_request()