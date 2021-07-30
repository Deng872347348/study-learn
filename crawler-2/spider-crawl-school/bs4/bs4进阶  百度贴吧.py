import requests
from  bs4 import BeautifulSoup
import os

headers={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}
def main(url):
    response=requests.get(url=url,headers=headers).text
    # print(response)
    soup=BeautifulSoup(response,'lxml')
    print(soup)
    title=soup.title.string
    print(title)
    detail_title=soup.select()
    print(detail_title)
if __name__ == '__main__':
    url='http://www.zongheng.com/'
    main(url)