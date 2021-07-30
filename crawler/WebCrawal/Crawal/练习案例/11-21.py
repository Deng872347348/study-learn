# 获取ulr
# 放弃请求
# 获取响应数据
#解析数据中的param和post请求
# 持久化数据
# import requests
# #指定url
# url='http://haokan.faloo.com/22/22627/'
# #获取页面数据
# page_text=requests.get(url=url).text
#
# #持久化数据
# with open("./无限.html",'w',encoding='utf-8') as fp:
#     fp.write(page_text)
#     print("爬取成功")import  requests
#import  requests
 # import json
 # if __name__=='__main__':
 #     posy_url='https://fanyi.baidu.com/langdetect'
 #     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#     }
#     #post请求参数处理，同get请求一致
#     word=input('enter a word:')
#     data={
#         'ke':word
#     }
#     #请求发送
#     response=requests.post(url=posy_url,data=data,headers=headers)
#     #获取响应数据：json()方法返回是obj,如果确认响应数据json，才可以使用json()
#     dic_obj=response.json()
#     #print(dic_obj)
#     #持久化数据
#     fileName=word+'.json'
#     fp=open(fileName,'w',encoding='utf-8')
#     json.dump(dic_obj,fp=fp,ensure_ascii=False)
#     print('over!!!')

import  requests
import  json
url='https://movie.douban.com/j/chart/tp_list'
param={
'type': '24',
'interval_id':'100:90',
 'action':'',
 'start':'60',
 'limit':'20',
 }
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
response=requests.get(url=url,params=param,headers=headers)
list_data=response.json()
fp=open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print("下载成功")

