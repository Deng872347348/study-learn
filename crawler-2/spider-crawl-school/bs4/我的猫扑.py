import requests
from bs4 import BeautifulSoup

class Youdao(object):

    def __init__(self):
        self.url = 'http://mpdzh.eastday.com/a/200717144503448446249.html?region=1'
        self.headers = {
            'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.114Safari / 537.36'
        }
    def post_data(self):
       response = requests.get(self.url,headers=self.headers).content.decode()
       # print(response)
       html=response
       return html

    def parse_data(self,data):
        soup = BeautifulSoup(data, 'lxml')
        # 文章的标题
        title = soup.title.string
        # print(str(title))
        # 文章的时间，
        time = soup.find('div',class_='post-header-t').find('span').text
        # print(time)
        # 文章的标题
        article_title=soup.find('div',class_='post-header').find('h2').text
        # print(article_title)
        # 文章的内容
        article_content=soup.find('div',class_='detail-article').find_all('p',limit=10)
        # print(article_content)
        article_p=""
        for p in article_content:
            article_p+=p.text+'\n'
        # print(article_p)
        self.save(title,time,article_title,article_p)
    def save(self,title,time,article_title,article_p):
        content={}
        content['网页标题']=title
        content['文章发布时间']=time
        content['文章标题']=article_title
        content['文章内容']=article_p
        with open('jueji.txt','w',encoding='utf-8') as f:
            f.write(str(content))


    def run(self):
        data = self.post_data()
        # print(data)
        self.parse_data(data)

if __name__ == '__main__':
    youdao = Youdao()
    youdao.run()
