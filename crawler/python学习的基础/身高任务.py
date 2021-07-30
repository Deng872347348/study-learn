    #输入身高，输出身高

# a=input()
# print(a)
import  random
#BMI的计算
# 在pycharm中新建python文件，要求输入身高和体重，计算BMI指数（体质指数，
#     是国际最常用来量度体重与身高比例的工具。它利用身高和
#     体重之间的比例去衡量一个人是否过瘦或过肥。）
# height=float(input("请输入身高："))
# weight=float(input("请输入体重："))
# BMI=round(weight/pow(height,2))#round 函数可以进行四舍五入
# if BMI<18.4:
#  print("偏瘦")
# elif BMI>=18.5 and BMI<23.9:
#  print("正常")
# elif BMI>=24.0 and BMI<27.9:
#  print("过重")
# elif BMI>=28.0:
#  print("肥胖")

# i=input()
# for i in range(0,11):
#  if (i==1):
# print(i)
# else:
# print('+')


# print("+"*11)
# print("+"+" "*9+         "+")
# print("+"*11)


# name = str(input("请输入你的姓名："))
# height = eval(input("请输入你的身高（m）:"))
# weight = eval(input("请输入你的体重（kg）:"))
# BMI = weight / pow(height,2)
# print("BMI值为：{:.2f}".format(BMI))#{:.2f}调用方法保留小数点后两位
# if BMI < 18.5:
#     print("您太瘦了，体重过轻，请加强营养！")
# else:
#     if 18.5 < BMI < 25:
#         print("恭喜您，您的身材非常好！")
#     else:
#         if 25 < BMI < 28:
#             print("您的身材有点偏胖，请请努力回到以前的标准身材！")
#         else:
#             if 28 < BMI < 32:
#                 print("您是一个小胖子，请注意饮食和加强锻炼！")
#             else:
#                 if BMI > 32:
#                     print("您严重肥胖，肥胖不好哟，要管住嘴、迈开腿！")

# for i in range(1,1001):
#       if i%3==2 and i%5==3 and i%7==2:
#             print("这个数就是",i)
#       else:
#        continue

#猜数字的游戏
# a = random.randint(1, 100)#产生一个随机数
#
# finished=0#开关，空循环是否执行
# while not finished:
#    guess=int(input("请输入一个随机数！"))
#    if guess==a:
#       print("恭喜你，猜对了")
#       finished=1
#    elif  guess<a:
#       print("你所猜的数字小了！")
#       print("系统给出的数字是",a)
#       finished=1
#    elif  guess>a:
#        print("你猜的数字太大了！")
#        print("系统给出的数字是", a)
#        finished=1
import  math
# a=10
# b=8
#
# print("最高的价格；",)
# print("最低的价格；",10)
# n = 1   # n表示当前项的数值
# s = 0   # s是累加求和变量
# ############### 编写下面的while循环代码 ###############
#
# while n <= 99:
#  if n % 2 ==0:
#        s = s-n
#  else:
#       s = s+n
#  n += n
#
# print(s)
for i in range(-6, 7):
    for j in range(-6, 7):
        if abs(i) + abs(j) == 6:
            print("*", end='')
        else:
            print(' ', end='')
    print()
