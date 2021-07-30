import requests
from lxml import etree
headers={
'ser-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

}
url='http://www.yingsx.com/1_1576/'
def get_url(url):
    resp=requests.get(url,headers=headers).content.decode()
    #print(resp)

    novel=etree.HTML(resp)
    chapter=novel.xpath("//div[@id='list']/dl/dd/a")
    #print(chapter)
    for a in chapter:
        chapter_li=a.xpath('./@href')[0]
        chapter_name=a.xpath('./text()')[0]
        # print(chapter_li)
        # print(chapter_name)
        new_url='http://www.yingsx.com'+chapter_li
        #print(new_url)
        #new_url(new_url)
        response = requests.get(new_url, headers=headers).content
        # print(response)
        novel_1 = etree.HTML(response)
        chapter = novel_1.xpath("//div[@class='box_con']")
        for a in chapter:
            chapter = a.xpath('//div[@id="content"]/text()')[0]
            #print(chapter
            with open('./圣墟小说.txt','ab') as f:
                f.write(chapter.encode('utf-8'))
                print(chapter_name+'下载成功')
# def new_url(new_url):
#     response = requests.get(new_url, headers=headers).content.decode()
#     # print(response)
#     novel_1=etree.HTML(response)
#     chapter = novel_1.xpath("//div[@class='box_con']")
#     for a in chapter:
#         chapter=a.xpath('./@id')
#         print(chapter)
if __name__ == '__main__':
    get_url(url)