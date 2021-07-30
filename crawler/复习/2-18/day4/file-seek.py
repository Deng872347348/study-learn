# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城


f = open("seek_write","w")
f.write("hello1\n")
f.write("hello2\n")
print("返回光标当前位置:",f.tell())
f.write("hello3\n")
print("返回光标当前位置:",f.tell())
f.seek(14)

f.write("-----")
