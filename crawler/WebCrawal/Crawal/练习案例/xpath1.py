#解析下载图片数据
#1、对http://pic.netbian.com/4kfengjing/发起请求，拿到页面源码数据
#2、对页面源码数据进行解析，解析出图片对应标签的src的属性值，也就是特定图片的url，再对这个url发请求，就可以拿到图片的数据
import requests
from lxml import etree
import os
if __name__=="__main__":
    #获取整张页面的源码数据
    url = "http://pic.netbian.com/4kfengjing/index_%d.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    #创建文件夹用于存放图片
    if not os.path.exists('./Piclibs'):
        os.mkdir('./Piclibs')
    #遍历列表
    for pageNum in range(1, 3):
        new_url = format(url % pageNum)  # format返回的是一个字符串，new_url就是对应分页的地址
        response = requests.get(url=new_url, headers=headers)
        # 手动设定响应数据的编码格式
        # response.encoding = 'utf-8' #为了解决标题乱码的问题，但只适应于一部分，对这个案例没有效果，所以可以对发生问题的地方进行指定的编码
        page_text = response.text
        # 实例化一个etree对象
        tree = etree.HTML(page_text)
        # 使用xpath进行数据解析，得到src和alt的属性值，也就是每一张图片的url和标题
        li_list = tree.xpath('//div[@class="slist"]/ul/li')  # 返回的是一批li标签

        for li in li_list:
            img_src = 'http://pic.netbian.com/4kfengjing'+li.xpath('./a/img/@src')[0] #获取属性值是用"/@tagName",返回的也是个列表，且只含有一个元素
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            #较为通用的处理中文乱码的方案
            img_name = img_name.encode('iso-8859-1').decode('gbk')#为了解决标题乱码的问题
            #print(img_name,img_src)
            #请求图片并进行持久化存储
            img_data = requests.get(url=img_src,headers=headers).content #注意图片是二进制数据，得用content属性
            img_path = 'Piclibs/'+img_name #定义图片存储的路径
            with open(img_path,'wb') as fp:  #多次打开文件夹用with更方便,写入二进制数据是用wb
                fp.write(img_data)
                print(img_name,'下载成功')