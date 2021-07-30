# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# staff_list = [
#     ["Alex",23,"CEO",66000],
#     ["黑姑娘",24,"行政",4000],
#     ["佩奇",26,"讲师",40000],
#     # [xxx,xx,xx,xxx]
#     # [xxx,xx,xx,xxx]
#     # [xxx,xx,xx,xxx]
#
#     ["佩奇",26,"讲师",40000],
# ]
# ["佩奇",26,"讲师",40000] in staff_list
#
# for i in staff_list:
#     if i[0] == "佩奇":
#         print(i[-1])
#         break
#

dic = {
    "Alex" :[23,"CEO",66000],
    "黑姑娘" :[24,"行政",4000],
    "佩奇": [26,"讲师",40000],

}

print("佩奇" in dic)

print(dic["佩奇"])
