import requests
import re
#导入库
#封装一个函数
#获取url
url='http://www.xbiquge.la/0/419/'
#伪请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
html_page=requests.get(url=url,headers=headers).content
html=html_page.decode()
print(html)
# toc_url_list = []
# toc_block = re.findall('<div id=list>(.*?)</div>', html, re.S)
# toc_url = re.findall('href="(.*?)"', toc_block, re.S)
# print(toc_url)
# print(toc_block)

 # for url in toc_url:
 #    toc_url_list.append(start_url + url)
 #     return toc_url_list

#if __name__=='__main__':
