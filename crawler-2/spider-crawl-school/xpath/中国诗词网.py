import requests
from lxml import etree
def get_url():
    url = 'http://www.zgshige.com/c/2020-07-26/14565212.shtml'
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
    }
    response=requests.get(url,headers).content.decode()
    html=etree.HTML(response)
    poet_title=html.xpath('//div[@class="text-center b-b b-2x b-lt"]/h3/text()')[0]
    poet_author=html.xpath('//div[@class="col-xs-12"]/span[1]/text()')
    poet_content=html.xpath('//div[@class="m-lg font14 mwebfont"]/p/text()')
    poet_author='\n'.join(poet_author)
    poet_content='\n'.join(poet_content)
    # print(poet_title)
    # print(poet_author)
    # print(poet_content)
    save(poet_title, poet_author, poet_content)
def save(poet_title, poet_author, poet_content):
    with open('中国诗词网.txt','a',encoding='UTF-8') as f:
        f.write(poet_title + '\n' + poet_author + '\n' + poet_content)
if __name__ == '__main__':
    get_url()