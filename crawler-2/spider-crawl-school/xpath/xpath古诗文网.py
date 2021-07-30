# coding=gbk
from lxml import etree
import requests
DATA = []

def getHTMLtext(url, headers, timeout=10):
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return ''


def xpathParser(text):
    htmlElement = etree.HTML(text)  # <class 'lxml.etree._Element'>
    name_list = htmlElement.xpath('/html/body/div[2]/div[1]/div/div[1]/p[1]/a/b/text()')
    dynasty_list = htmlElement.xpath('/html/body/div[2]/div[1]/div/div[1]/p[2]/a[1]/text()')
    author_list = htmlElement.xpath('/html/body/div[2]/div[1]/div/div[1]/p[2]/a[2]/text()')
    content_list = []
    poetries = htmlElement.xpath(
        '//div[@class="contson" and contains(@id,"contson")]')  # 返回一个列表，里面每一个都是'lxml.etree._Element'
    # print(etree.tostring(poetries[0],encoding = 'utf-8').decode('utf-8'))
    for poetry in poetries:
        row_content = ''.join(poetry.xpath('.//text()'))  # 这里的.可千万不能掉，否则会忽略掉poetry哦
        content_list.append(row_content.replace('\n', ''))
    row_likes_list = htmlElement.xpath('//a[contains(@id,"agood")]/span/text()')
    likes_list = [int(like.strip()) for like in row_likes_list]
    for value in zip(name_list, dynasty_list, author_list, content_list, likes_list):
        name, dynasty, author, content, likes = value
        poetry_dict = {
            '诗词名': name,
            '朝代': dynasty,
            '作者': author,
            '内容': content,
            '点赞数': likes
        }
        DATA.append(poetry_dict)


def print_poetry(data):
    for every_poetry in data:
        print(every_poetry['诗词名'])
        print(every_poetry['朝代'] + ':' + every_poetry['作者'])
        print(every_poetry['内容'])
        print('有{}人喜欢这首诗(词)哦'.format(every_poetry["点赞数"]))
        print("\n" + '*' * 50 + "\n")


if __name__ == '__main__':
    row_url = 'https://www.gushiwen.org/default_{}.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    num = input('请输入要爬取的页数（1-100）:')
    for i in range(eval(num)):
        url = row_url.format(i + 1)
        text = getHTMLtext(url, headers)
        if text == '':
            print('url: {} 访问失败'.format(url))
        else:
            xpathParser(text)
    DATA.sort(key=lambda x: int(x['点赞数']), reverse=True)
    TOP10 = DATA[:10]
    print_poetry(TOP10)
