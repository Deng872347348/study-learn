#需求：爬取三国演小说的所有章节标题和章节内容  https://www.shicimingju.com/book/sanguoyanyi.html
# 思路：先使用通用爬虫爬取整张页面，再进行数据解析获取标题和章节所对应的链接的地址，再通过获取的详情页的链接获取每个章节的数据，
import  requests
from bs4 import BeautifulSoup
if __name__=="__main__":

    #对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    #发起请求并获取数据
    page_text = requests.get(url = url,headers = headers).text
    #在首页中解析出标题和详情页的url
    #1、实例化一个BeautiSoup对象，需要将总页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li') #返回的是存放一系列li标签的列表

    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        #在主页面中每一个标题都可以点击，说明标题存在于a标签内
        title = li.a.string #获取li标签中的a标签中的字符串
        detail_url = 'https://www.shicimingju.com'+li.a['href'] #完整的详情页的url
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url = detail_url,headers = headers).text  #获取详情页对应的数据
        #从detail_page_text中解析出章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')