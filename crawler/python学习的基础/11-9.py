# import requests
# url='https://www.baidu.com/'
# response=requests.get(url)
# print(response.status_code)
# result=response.content.decode('utf-8')
# print(result)

#学习时间：2020/11/9 15:09
# import requests
# url='https://www.baidu.com/'
# response=requests.get(url)
# print(response.status_code)
# result=response.content.decode('utf-8')
# print(result)

#如何提取<title>百度一下，你就知道</title>
# import re
# result1=re.match(r'<title>.*</title>',result,re.S|re.M)
# print(result1)
# result1=re.search(r'<title>.*</title>',result,re.S|re.M)
# print(result1)
# print(result1.group())#提取<title>百度一下，你就知道</title>
#
# result=str1.replace("<p>",'').replace('<p>','').replace('-','').replace('<div>','').replace('')


# for i in range(1000,3000):
#     if i%7==0 and i%5!=0:
#         num=i
#         i.append(num)
#         print(str(l).replace('[','').replace(']','').replace(' ',''))

        #
        # l=str([x for  x in values if x% !=0])
        # print(''.join(l.split()).replace('[','').replace(']',''))
# values = input()
# L=[]
# ########## Begin ##########
# ss=list(filter(lambda x: x % 2 == 1 , values))
# print(ss)
#print(''.join(L.split()).replace('[','').replace(']',''))

        # try:
        #     list[2]+list[7]
        #     print(num)
        # except TypeError as e:
        #     print()
        #     print(str(list1[2]+str(list[7])))
        #
        #     print("数组下标越界")
# string="happy new year"
# print(string[3:8])
for var in range(0,10):
    print(var)