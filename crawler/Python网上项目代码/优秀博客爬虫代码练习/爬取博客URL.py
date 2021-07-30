# -*- coding:utf8 -*-
import string
import re
import time
import random
import requests
class CSDN_Spider:

    def __init__(self, url):
        self.myUrl = url
        self.datas = []
        print( u"csdn爬虫已启动....")

    def csdn(self):
        url = self.myUrl + "?viewmode=list"
        headers={
            'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
        }
        rep = requests.get(url=url,headers=headers)
        mypage = rep.content.decode("utf8")
        print(mypage)
        Pagenum = self.page_counter(mypage)
        # print Pagenum
        self.find_data(self.myUrl, Pagenum)

    def page_counter(self, mypage):  # <a href="/djd1234567/article/list/11">尾页</a>
        myMatch = re.search(u'/article/list/(\d+?)">尾页</a>', mypage, re.S)

        if myMatch:
            Pagenum = int(myMatch.group(1))
            print(u"爬虫报告:发现目录一共%d页" % Pagenum)
        else:
            Pagenum = 0
            print(u"爬虫报告:没找到页面的数量")

        return Pagenum

    def find_data(self, myurl, Pagenum):

        name = myurl.split("/")
        f = open(name[-1] + '.txt', 'w+')

        for i in range(1, Pagenum + 1):
            print(i)
            print(u"爬虫报告:第%d页正在加载中......" % i)

            url = myurl + "/article/list/" + str(i)
            headers = {
                'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
            }
            mypage=requests.get(url=url,headers=headers).text
            myItems = re.findall(u'"><a href="/' + myurl.split("/")[-1] + '/article/details/(\d+?)" title="', mypage,re.S)
            # print myItems
            for item in myItems:
                self.datas.append(item + "\n")

            # time.sleep(1)

        f.writelines(self.datas)
        f.close()

        print(self.datas)

        print(u"爬虫报告:文件已下载到本地并打包成txt格式文件")

if __name__ == '__main__':

 url = "https://blog.csdn.net/Deng872347348"

 mySpider = CSDN_Spider(url)
 mySpider.csdn()