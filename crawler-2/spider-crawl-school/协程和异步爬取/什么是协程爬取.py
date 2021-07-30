from gevent import monkey
monkey.patch_all()
import gevent,time,requests
start = time.time()
url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']
def crawler(url):
  for url in url_list:
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)