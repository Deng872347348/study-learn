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
        '//div[@class="contson" and contains(@id,"contson")]')  # ����һ���б�����ÿһ������'lxml.etree._Element'
    # print(etree.tostring(poetries[0],encoding = 'utf-8').decode('utf-8'))
    for poetry in poetries:
        row_content = ''.join(poetry.xpath('.//text()'))  # �����.��ǧ���ܵ����������Ե�poetryŶ
        content_list.append(row_content.replace('\n', ''))
    row_likes_list = htmlElement.xpath('//a[contains(@id,"agood")]/span/text()')
    likes_list = [int(like.strip()) for like in row_likes_list]
    for value in zip(name_list, dynasty_list, author_list, content_list, likes_list):
        name, dynasty, author, content, likes = value
        poetry_dict = {
            'ʫ����': name,
            '����': dynasty,
            '����': author,
            '����': content,
            '������': likes
        }
        DATA.append(poetry_dict)


def print_poetry(data):
    for every_poetry in data:
        print(every_poetry['ʫ����'])
        print(every_poetry['����'] + ':' + every_poetry['����'])
        print(every_poetry['����'])
        print('��{}��ϲ������ʫ(��)Ŷ'.format(every_poetry["������"]))
        print("\n" + '*' * 50 + "\n")


if __name__ == '__main__':
    row_url = 'https://www.gushiwen.org/default_{}.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    num = input('������Ҫ��ȡ��ҳ����1-100��:')
    for i in range(eval(num)):
        url = row_url.format(i + 1)
        text = getHTMLtext(url, headers)
        if text == '':
            print('url: {} ����ʧ��'.format(url))
        else:
            xpathParser(text)
    DATA.sort(key=lambda x: int(x['������']), reverse=True)
    TOP10 = DATA[:10]
    print_poetry(TOP10)
