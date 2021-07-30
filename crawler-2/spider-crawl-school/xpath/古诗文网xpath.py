import requests
from lxml import etree

def get_url():
    url='https://so.gushiwen.org/shiwenv_a1e7559dada7.aspx'
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
    }
    response=requests.get(url,headers=headers).text
    html=etree.HTML(response)
    poet=html.xpath('//div[@class="left"]/div[@id="sonsyuanwen"]')
    for i in poet:
        poet_title=i.xpath('./div[@class="cont"]/h1/text()')[0]
        poet_content=i.xpath('./div[@class="cont"]/div[@id="contsona1e7559dada7"]/text()')
        poet_content='\n'.join(poet_content)
        poet_author=i.xpath('./div/p/a/text()')
        poet_author=''.join(poet_author)
        # print(poet_title)
        # print(poet_author)
        # print(poet_content)
    save(poet_title,poet_author,poet_content)
def save(poet_title,poet_author,poet_content):
    with open('古诗文网.txt','a',encoding='UTF-8') as f:
        f.write(poet_title+'\n'+poet_author+'\n'+poet_content)
if __name__ == '__main__':
    get_url()

