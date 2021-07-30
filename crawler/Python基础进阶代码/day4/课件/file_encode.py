# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

f = open("gbk_file2","wb")
f.write("哈".encode("gbk") )  # 写入的文本要用字节类型


# f = open("/Users/alex/Downloads/1589450091035.jpg")
# for line in f:
#     print(line)