# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

f = open("嫩模联系方式","r+")
print(f.readline())
print(f.tell()) # 52
f.seek(f.tell())
f.write("-又来了一个新模特....")