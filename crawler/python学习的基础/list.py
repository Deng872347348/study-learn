#nba=["迈克尔·乔丹","比尔·拉塞尔","卡里姆·阿卜杜尔·贾巴尔","威尔特·张伯伦","埃尔文·约翰逊","科比·布莱恩特","蒂姆·邓肯","勒布朗·詹姆斯"]
# a=[nba[1],nba[2],nba[3],nba[4]]
# print(a)
# print(nba[0:5:2],end=' ')
# nba.reverse()
# print(nba[::-1],end=' ')

# import easygui   as g
# import sys
#
# while 1:
#     g.msgbox("嗨，欢迎进入第一个界面小游戏“)
#     msg = "请问你希望在邓波的世界里面学到什么知识呢”
#     title = "小游戏互动"
#     choices = ["谈恋爱"，"编程", "打游戏", "画画"]
#
#
#     g.msgbox("你的选择是：" + str(choice), "结果")
#     msg = "你希望重新开始吗？"
#     title =“请选择“
#     if g.ccbox=(msg, title):
#         pass
#     else:
#         sys.exit(0)

# list1 = [2, 3, -43, 4, 5, -5, 4, -535, 34, 5, 345, -3, 45, 3, 6, 345, -546, 546, 34, -56, 34, 5, 86, 7, 0, 12341, 979,
#          7, 67, -856, 454, 8, -64, 342, -63, 568]

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########### Begin ###########
# 使用列表推导式来复制给定的列表，并筛选掉其中的负数，打印复制后的列表



# def positive_number(LL):
#     L = [i for i in LL if i >= 0]
#     print(L)
# l = [1,2,3,45,8,3,1,-56,-4,0]
# positive_number(l)

# def  post(ll):
#     l=[i for i in ll if i>=0]
#     print(l)
# list1 = [2, 3, -43, 4, 5, -5, 4, -535, 34, 5, 345, -3, 45, 3, 6, 345, -546, 546, 34, -56, 34, 5, 86, 7, 0, 12341, 979,
#          7, 67, -856, 454, 8, -64, 342, -63, 568]
# post(list1)

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# name=[i for i in names if len(i)>5  ]
# print(name)
# print(names[0][2])
# nba=["迈克尔·乔丹","比尔·拉塞尔","卡里姆·阿卜杜尔·贾巴尔","威尔特·张伯伦","埃尔文·约翰逊","科比·布莱恩特","蒂姆·邓肯","勒布朗·詹姆斯"]
# for index, value in enumerate(nba):
#     print (index, value)

        # price=[1200,5330,2988,6200,1998,8888]
        # price1 = [i for i in price if i>5000 ]
        # print(price1)

# while trycount < 3:
#     inuser = input("用户名:")
#     inpasswd = input("密码:")
#     trycount+=1
#     if inuser in users:
#         index = users.index(inuser)
#         passwd = passwds[index]
#         if inpasswd == passwd:
#             print("%s登陆成功" % (inuser))
#             break
#         else:
#             print("%s登陆失败: 密码错误!" % (inuser))
#     else:
#         print("用户%s不存在" % (inuser))
# else:
#     print("已经超过三次机会")
users = ['root','westos']
passwds = ['123','456']
trycount = 0
while trycount < 3:
# for i in range(1,4):
    inuser = input("用户名:")
    inpasswd = input("密码:")
    trycount += 1

    if inuser in users:
        index = users.index(inuser)
        passwd =passwds[index]
        if inpasswd == passwd:
            print("%s登陆成功" % (inuser))
            break
        else:
            print("%s登陆失败: 密码错误!" % (inuser))
    else:
        print("用户%s不存在" % (inuser))
else:
    print("已经超过三次机会")