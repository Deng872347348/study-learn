# for i in (0,10):
#     #print('%d*%d' % (i, j), end='\n')
#     for j in (0,i+1):
#         print('%d*%d'%(i,j),end='\n')


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end="  ")  #end= 以。。。结尾
#     print()

# for i in range(1,9):
#     for j in range(1,i+i):
#         print(i,'*',j,'=','i*j',end='\n')
#     print()
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{0}x{1}={2}".format(i,j,j*i),end="  ")  #end= 以。。。结尾
#     print()

# def Verification(func):  # func表示一个函数
#     def b():
#         username =input()
#         password = input()
#         if username=='educoder' and password == '123456':
#             func()
#         else:
#             print("账号密码错误")
#
#     return b()
# ########## End ##########
# @Verification
# def C():
#   print("登录成功")
# #res=Verification(C)
# #C()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(0,20)  #linspace()函数指定横坐标范围
# plt.plot(x,.5+x)
# plt.plot(x,1+2*x,'--')
# plt.show()

# start = int(input())     # 读取内容的开始位置
# end = int(input())     # 读取内容的结束位置
# f=open('数据集说明.txt','a',encoding='utf-8')
# #print(type(f))
# #f.write('俄罗斯媒体分析，美军抢占叙利亚油田有诸多战略考量：叙利亚三分之一的石油资源集中在叙北部和东部地区，通过控制这些石油收'
#         '入，把这一“钱袋子”紧攥在自己手中，美国可以加强对叙库尔德武装的控制。同时，也可阻碍叙利亚政府正在实施的战后重建。此外'
#         '，驻叙美军不仅挑衅、拦截在叙北地区土俄的巡逻车队，而且还怂恿库尔德武装和民众沿途'
#         '围堵、袭击俄军，向俄军装甲车开枪，投掷自制燃烧弹等。而美国驻叙利亚和打击“伊斯兰国”国际军事联盟特使杰弗里更是赤裸裸地表示，驻叙美军的'
#         '任务是，为俄罗斯制造一个如新越南或新阿富汗一样的“战争泥潭”，而非打击恐怖主义。')
#
# f.close()
# start = int(input())     # 读取内容的开始位置
# end = int(input())     # 读取内容的结束位置
# f = open("数据集说明.txt", "r",encoding='utf-8')
# # 读取的数据
# str = f.read()[start:end]
# print ("读取的数据是: ", str)
# f.close()
#获取当前的时间：

# import  time
# print(time.strftime('%Y %m %d %H %M %S',time.gmtime()))




# start = int(input())     # 读取内容的开始位置
# end = int(input())     # 读取内容的结束位置

# f = open('数据集说明.txt','w',encoding='utf-8')
# result = list()
# for line in f.readlines():                # 逐行读取数据
#    line = line.strip()                #去掉每行头尾空白
#    if not len(line) or line.startswith('#'):   # 判断是否是空行或注释行
#       continue                 #是的话，跳过不处理
#    result.append(line)              #保存
#    result.sort()                       #排序结果
# print (result)
# open('cdays-4-result.txt','w').write('%s' % '\n'.join(result))        #保存入结果文件
# 闭包：


# 装饰器:装饰器可以添加函数，也可以添加参数
