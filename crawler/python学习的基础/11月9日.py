# string='DengBo'
# for i in string:
#     print(ord(i))
#     #ord()函数可以计算字符串的asci编码
# string="我爱中国"
# data=string.encode('utf-8')
# result=data.decode('utf-8')
# print(data)
# print(result)
# import re
# text = input()
# #********** Begin *********#
# # #1.匹配以t开头的所有单词并显示
# # itext = re.finditer(r'^t+',text)
# # for j in itext:
# #     # print(i)
# #     print(j.group())
# #     # print(i.span())
# itext = re.finditer(r'^t+',text, )
# for j in itext:
#     # print(i)
#     print(j.group())
# #2.用空格分割句子
# print(re.split("\s+",text ))
# #3.用‘-’代替句子中的空格
# print(re.sub( r'\s','-', text))
# #4.用‘-’代替句子中的空格，并返回替换次数
# print(re.subn('\s+','-',text) )
# #********** End **********#
# from functools import reduce
#
# x = reduce(lambda x,y:x+y,[int(x) for x in "1" *10])
# print([int(x) for x in "1" *10])


# txt = "Hello, welcome to my world."
#
# x = txt.endswith(".")
#
# print(x)

x='D:\pycharm.ext'
y=x.endswith('.exe')
print(y)