# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

f = open("嫩模联系方式")
print(f.readlines())
for line in f: # one loop, one line
    line = line.split()
    #print(line)
    height = int(line[3])
    weight = int(line[4])
    if height >= 170 and weight <= 50:
        print(line)

