import requests
import re
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
def geturls():
    url='http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm'
    headers={
        'User - Agent':'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 86.0) Gecko / 20100101Firefox / 86.0'
    }
    response=requests.get(url,headers).content.decode()
    # res = '<a href="(.*?)" target=.*?</a>'
    res='<a href="(.*?)" target=.*?<strong>.*?</strong>'
    ss = re.findall(res, response, re.S)
    urls=ss[1:]
    return urls
    # print(urls)

def parsepage(url):
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
    # return mainbody
if __name__ == "__main__":
    urls = geturls()
    parsepage(urls)
