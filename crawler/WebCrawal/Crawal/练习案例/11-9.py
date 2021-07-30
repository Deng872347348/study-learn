# import requests
# import  re
# url='https://www.baidu.com/'
# response=requests.get(url)
# print(response.status_code)
# result=response.content.decode('utf-8')
# print(result)
# S1=re.match(r'<title>.*<\/title>',result,re.S|re.M)
# print(S1)
# S2=re.search(r'<title>.*<\/title>',result,re.S|re.M)
# print(S2)
# print(S2.group())
#
# S3=re.findall(r'<title>(.*)<\/title>',result,re.S|re.M)
# print(S3[0])

import re

input_str = input()

# 编写获取(任意字符)+ython的字符串，并存储到变量a中
########## Begin ##########
a=re.findall(r'.+ython',input_str,re.S|re.M)

########## End ##########
print(a)
