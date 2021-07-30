# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

a = "Alex li 金角大王"

print(a.center(50,"-"))  # output : --------------------Alex 金角大王---------------------

print(a.count("l",0,4))
print(a.endswith("王八")) # False 判断结尾
print(a.startswith("Alex")) # False 判断开头

print(a.find("i"))  # 字符查找，返回-1代表没找到，如果找到了，就返回所查字符的索引

print(a.isdigit())
print("22".isdigit()) # 判断是否是整数

l = ["alex","black girl","peiqi"]
print("-".join(l)) # 拼接字符串， alex-black girl-peiqi

print(a.replace("l","M" ,1)) # 字符串替换， output: AMex li 金角大王

print(a.split("l",1))  # 字符串分割 output: ['A', 'ex li 金角大王']
