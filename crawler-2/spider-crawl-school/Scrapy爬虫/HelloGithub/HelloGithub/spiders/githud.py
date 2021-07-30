import scrapy
from  scrapy.http import Request,FormRequest
from  ..items import HellogithubItem
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
class GithudSpider(scrapy.Spider):
    name = 'githud'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']
    headers={
        "User-Agent": UserAgent().random
    }
    #重写开始satrt-request
    def start_requests(self):
        urls=['https://github.com/login']
        for url in urls:
            yield Request(url,meta={'cookiejar':1},callback=self.github_login)
    #模拟登录
    def github_login(self,response):
        soup=BeautifulSoup(response.text,'lxml')
        authenticity_token=soup.select('div#login input')[0].attrs['value']
        self.logger.info('authenticity_token:'+authenticity_token)
        #FormRequest类发送表单请求
        return FormRequest.from_response(response,meta={'cookiejar':response.meta['cookiejar']},
                                         url='https://github.com/session',
                                         headers=self.headers,
                                         formdata={
                                             
                                         },
                                         callback=self.github_after,
                                         dont_click=True
                                         )
    #验证登录成功，并且获取用户名
    def github_after(self,response):
        soup=BeautifulSoup(response.text,'lxml')
        username=soup.find('a',class_='').text
        if username:
            self.logger.info('登录成功.用户名:'+username)
            #请求头登入我的个人信息
            return Request('https://github.com/',
                           meta={'cookiejar': response.meta['cookiejar']},
                           callback=self.parse_page
                           )
        else:
            self.logger.info('登录失败')
    #个人首页信息
    def parse_page(self,response):
        if response.status==200:
            item=[]
            soup=BeautifulSoup(response.text,'lxml')
            li_list=soup.select('ol li')
            for li in li_list:
                projectName=li.find('span',class_='repo').text
                info=li.find('p',class_='').text
                item=HellogithubItem()
                item['projectName']=projectName
                item['info']=info.replace(' ','').replace('\n','')
                item.append(item)
        return item
