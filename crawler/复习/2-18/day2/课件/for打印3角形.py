# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城


# n = 10
#
# for i in range(n):
#     if i < 5:
#         print(i*"*")
#     else:
#         print( (n-i) * "*")


# 打印 四角形
n = 10
for i in range(n):
    if i < 5:
        s = i * "#"
    else:
        s = (n-i) * "#"
    print(s.center(20," "))