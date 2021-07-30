# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

f = open("快递信息.csv")

add_list= []
for line in f:
    name,region,*addr= line.split(",")
    region = "".join(region.split())
    if len(name) >1:
        name = name.replace(name[1],"*")
    else:
        name += "*"
    add_list.append(
        [name,region+"".join(addr).strip()]
    )

mail_addrs = {}

for i in add_list:
    region = i[1][0:3]
    if region not in mail_addrs:
        mail_addrs[region] = [ i ]
    else:
        mail_addrs[region].append(i)

print(mail_addrs)

for k,v in mail_addrs.items():
    print(k,v)