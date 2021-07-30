# 1、程序运行时，让用户输入工资大小。
# 2、列出当所有产品列表清单。
# 3、让用户输入需要购买的产品编号。
# 4、结束程序时，打印购买明细与剩下余额。
# shopping_list = [('Iphone',5000),('MacBook',9000),('Huwei P20',9999)]
# shopping_car = []
# salary = int(input('请输入你的工资:'))
# while True:
#     for index,item in enumerate(shopping_list):
#         print(index,item)
#     user_change = input('请输入你要购买的产品编号：')
#     if user_change.isdigit():
#         user_change=int(user_change)
#         if user_change >= 0 and user_change < len(shopping_list) and salary >= shopping_list[user_change][1]:
#             shopping_car.append(shopping_list[user_change])
#             salary -=shopping_list[user_change][1]
#         elif salary <= shopping_list[user_change][1] :
#             print('你的余额已经不足！！！，请让你的工资变得更多     ')
#         else:
#             print('你输入的编号有误，请重新输入！！！！！')
#     elif user_change == 'q':
#         print('--------已购买的产品-------')
#         print(shopping_car)
#         print('剩下的余额为>>>：',salary)
#         exit()
#     else:
#         print("输入有误，请重新输入")
# tup = (1,"3",4,5,"4","a",(1,2,3,4),"b","c",6,17,"d",("a","b","c"),0,"e","f",True,10,"False",11,"h","A","B","C",30,"D",-35,-60,(-1,-2,-5))
#
# list=list(tup)
# list1=[]
# for i in list:
#  if type(i)!=int:
#   list1.append(i)
# tup1=tuple(list1)
# print(tup1)


# v = str(input())
# k = str(input())
# dict1 = {'北京': '北京', '山东': '济南'}
#
# for k, v in dict1.items():
#  if str(k) != str(v):
#
#   dict1[k] = v
#  else:
#   dict1[k] = v
#
# print(dict1)