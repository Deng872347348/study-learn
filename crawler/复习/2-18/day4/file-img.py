# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# f = open("1589450091035.jpg","rb")
# for line in f:
#     print(line)

# name = ""
# name = None  # 空值


# encoding=None ， 告诉你的解释器， 当前 要打开的这个文件 是什么编码
# 如果是None, 则用解释器默认编码，utf-8


# wb 二进制写
f = open("wb_file","wb")

s = "路飞"
#f.write(s.encode("gbk"))
# print(s.encode("utf-8"))
# f.write(s.encode("utf-8"))
f.write("路飞")

