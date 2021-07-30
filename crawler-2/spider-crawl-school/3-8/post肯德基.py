import requests
import csv
#确定爬取的url地址
url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
#确定搜索的关键字
keyword=input("请输入搜索关键字")
param={
'cname':'',
'pid':'',
'keyword':keyword,
'pageIndex':1,
'pageSize':10,
}
#构建请求头
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}
#发送http请求
response=requests.post(url=url,data=param,headers=headers)
#得到网站的响应信息
html=response.text
print(html,type(html))
content=response.json() #转成了字典
print(content,type(content))
print(content)
info_list=content['Table1']    #json数据的解析
print(info_list)
# for info in info_list:
#     storeName=info['storeName']+"餐厅"
#     addressDetail=info['addressDetail']
#     cityName=info['cityName']
#     print(storeName,addressDetail,cityName)

# #数据持久化存储
# with open("baidusearch.html",'w',encoding='utf-8') as f:
#     f.write(html)
#csv存储
# with open("kengdeji.csv",'a',encoding='utf-8',newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow([storeName,addressDetail,cityName])
