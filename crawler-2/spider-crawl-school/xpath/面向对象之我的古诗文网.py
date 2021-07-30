from lxml import etree
import requests

class Youdao(object):
    #构建请求头
    def __int__(self,url,headers):
        self.url =url
        self.headers =headers
    #解析请求头，并且发起请求
    def get_url(self,url,headers):
        response = requests.get(url, headers)
        # print(response)
        return response.text
    #进行xpath解析
    def get_xpath(self,data):
        html = etree.HTML(data)
        poet=html.xpath('//div[@class="left"]/div[@id="sonsyuanwen"]')
        for i in poet:
            poet_title = i.xpath('./div[@class="cont"]/h1/text()')[0]
            poet_content = i.xpath('./div[@class="cont"]/div[@id="contsona1e7559dada7"]/text()')
            poet_content = '\n'.join(poet_content)
            poet_author = i.xpath('./div/p/a/text()')
            poet_author = ''.join(poet_author)
        self.save(poet_title,poet_author,poet_content)
    #数据存储函数
    def save(self,poet_title,poet_author,poet_content):
        with open("古诗文.txt",'a',encoding='utf-8') as f:
            f.write(poet_title+'\n'+poet_author+'\n'+poet_content)
    def run(self):
        url='https://so.gushiwen.org/shiwenv_a1e7559dada7.aspx'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        data=self.get_url(url,headers)
        self.get_xpath(data)
if __name__ == '__main__':
    Youdao().run()