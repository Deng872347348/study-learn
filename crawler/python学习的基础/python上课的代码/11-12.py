# #正则的分组
#
#
# import re
# string='<div><a href="#">星期一</a></div>'
# result=re.search(r'(<a.*>)(.*)(<\/a>)',string,re.S)
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# def function_tips():
#     '''功能：每天输出一条励志文字
#     '''
#     import  time #得到时间戳
#     import datetime                                 # 导入日期时间类
#     # 定义一个列表
#     mot = ["今天星期一:\n坚持下去不是因为我很坚强，而是因为我别无选择",
#           "今天星期二:\n含泪播种的人一定能笑着收获",
#           "今天星期三:\n做对的事情比把事情做对重要",
#           "今天星期四:\n命运给予我们的不是失望之酒，而是机会之杯",
#           "今天星期五:\n不要等到明天，明天太遥远，今天就行动",
#           "今天星期六:\n求知若饥，虚心若愚",
#           "今天星期日:\n成功将属于哪些从来不说“不可能”的人"]
#     day = datetime.datetime.now().weekday()         # 获取当期星期
#     print(mot[day])                                 # 输出每日一贴
# function_tips()          # 调用函数
# import  datetime
# day=datetime.datetime.now().weekday()
# date=datetime.datetime.now()
# print(day)
# print(date.year)
# print(date.month)
# print(date.day)
#四种形参：位置参数，默认参数，关键字参数，可变参数


#解包序列重点！！！！方法 .*列表对象  *元组对象  **字典  解包字典
def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm
print(lcm(8,9))