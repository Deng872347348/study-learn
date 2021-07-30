import requests
from lxml import etree
import time
import os
def main():
    url = 'https://music.163.com/discover/toplist'#?id=3778678
    response = requests.get(url)
    data = etree.HTML(response.text)
    a_list = data.xpath('//a[contains(@href,"/song?")]')
    # print(a_list)
    for a in a_list:
        href = a.xpath('./@href')[0]
        id = href.split('=')[1]
        # print(href)
        name=a.xpath('./text()')[0]
        #print(name)
        music_url = 'http://music.163.com/song/media/outer/url?id=' + id
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        resp = requests.get(music_url, headers=headers)
        # print(resp)
        path='网易云热歌'
        if not os.path.exists(path):
            os.mkdir(path)
        time.sleep(2)
        with open(path+'./music%s.mp3'%name,'wb') as file:
           file.write(resp.content)
        print(name+"下载成功")
if __name__ == '__main__':
            main()
