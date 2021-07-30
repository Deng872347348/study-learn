import requests
from pyquery import PyQuery as pq

"""
1.需要得到网页的请求数据
    url
    headers
    response 发送请求，返回响应

2.提取数据
    提取到图片的url 

3.保存图片到本地
请求图片地址 并且保存到本地 
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

count = 1
# 1.需要得到网页的请求数据
def RequestIndex(page):

#     url

    url = 'https://www.buxiuse.com/?page={}'.format(page)

#     headers


#     response 发送请求，返回响应

    r = requests.get(url, headers=headers).text
    # print(r.text)
    return r


#
# 2.提取数据
def dataEX(index):
#  数据初始化
   doc = pq(index)
#     提取到图片的url

   height_min = doc('.height_min').items() #用于多个节点结果 遍历获取 转化成数据集 遍历

   for i in height_min:

       imgUrl = (i.attr('src'))
       print(imgUrl)
       ImgSave(imgUrl)

# 3.保存图片到本地
# 请求图片地址 并且保存到本地
def ImgSave(imgUrl):
    global count

    response = requests.get(imgUrl,headers=headers)
    # print(response)
    with open('./不羞涩社区小姐姐们/{}.jpg'.format(count),"wb") as  f:
        f.write(response.content)
        count += 1


if __name__ == '__main__':
    for page in range(1,10):
       index =  RequestIndex(page)
       dataEX(index)