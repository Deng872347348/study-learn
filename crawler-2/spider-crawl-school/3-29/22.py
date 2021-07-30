import requests
from lxml import etree
import  re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}



def parsepage(url):
	# ********** Begin ********** #
    #一级页面的xpath解析
   response=requests.get(url=url,headers=headers).content.decode()
   # html_xpath=etree.HTML(response)
   # html=html_xpath.xpath('//div[@class="text"]/div[@class="clipboard_text"]/div[@class="highlight"]/p')
   # print(html)
   # ss = []
   # for a in html:
   #      #a标签的href
   #      href=a.xpath('./a/@href')
   #      if href==[]:
   #          continue
   #      else:
   #        urls=''.join(href)
   #        print(urls)
   #一级页面的数据提取，用正则
   res = '<a href="(.*?)" target=.*?<strong>.*?</strong>'
   ss = re.findall(res, response, re.S)
   urls = ss[1:]
   # print(urls)
   second_page(urls)
#定义二级页面解析的函数
def second_page(urls):
    # mainbody = []  # 保存新闻内容
    # for url in urls:
    #     response = requests.get(url=url, headers=headers).content.decode()
    #     second_page = etree.HTML(response)
    #     second_html = second_page.xpath('//div[@class="inner"]')
    #     for a  in second_html:
    #         # 获取图片的url
    #                 secnod_url=a.xpath('//div[@class="clipboard_text"]/div[@class="highlight"]/p/img/@src')
    #
    #                 # 获取标题并去除首尾空格
    #                 second_title=a.xpath('./h1/text()')
    #                 second_title=''.join(second_title).strip()
    #                 # 获取作者并去除首尾空格
    #                 second_author=a.xpath('.//span[@class="appellation"][2]/text()')
    #                 second_author=''.join(second_author).strip()
    #                 # 获取正文并去除首尾空格
    #                 second_article=a.xpath('//div[@class="text"]/div[@class="clipboard_text"]/div[@class="highlight"]/p/text()')
    #                 second_article=''.join(second_article).strip()
    #                 print(second_title,second_author,second_article)
    mainbody = []  # 保存新闻内容
    for url in urls:
        response = requests.get(url, headers=headers)
        result = response.content.decode("utf8")
        html = etree.HTML(result)
        img = html.xpath('//div[@class="highlight"]//p//img//@scr')

        # 获取图片的url
        imgurl = []
        split_url = url.split("/")
        split_url.pop(-1)
        if len(img) >= 1:
            for x in img:
                imgurl.append("/".join(split_url) + "/" + x)
        else:
            imgurl = ""

        # 获取标题并去除首尾空格
        title = "".join(html.xpath('//div[@class="row"]//div[@class="inner"]//h1/text()')).strip()

        # 获取作者并去除首尾空格
        author = (html.xpath('//div[@class="row"]//span[@class="appellation"]//text()')[-1].split(":")[-1]).strip()

        # 获取正文并去除首尾空格
        cont = html.xpath(
            '//div[@class="content"]//div[@class="highlight"]/p//*[not(@color="navy")]/text()|//div[@class="highlight"]/p/text()')
        content = "".join(cont).strip()
        mainbody.append({"title": title, "author": author, "content": content, "imgurl": imgurl})
        print(mainbody)
if __name__ == '__main__':
    url='http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm'
    parsepage(url)




