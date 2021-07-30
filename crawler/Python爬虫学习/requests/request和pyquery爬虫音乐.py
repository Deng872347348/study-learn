import  requests
import os
from pyquery import    PyQuery as pq
import time
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

}
def RequestsIndex():
    url='https://music.163.com/discover/toplist?id=19723756'
    response=requests.get(url,headers=headers).text
    #print(response.text)
    return  response
#数据得一个提取
def dataEx(index):
    doc=pq(index)
    #print(doc)
    music=doc('.txt').items()
    #print(music)
    for i in music:
        music=(i.attr('data-res-id'))
        print(music)
if __name__ == '__main__':
    index=RequestsIndex()
    dataEx(index)
