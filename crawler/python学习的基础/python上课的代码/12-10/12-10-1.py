# ss = eval(input())
# num = 0
#
# for i in ss:
#     try:
#         num += i
#         type(i)==int
#     except:
#         continue
#
# print(num)
# f = open("src/step1/test.txt", "r")
#
# eval(input())
# if f.read() or f.seek(3) or f.readlines():
#   print("文件已关闭")
# elif f.write():
#  print("错误信息为write() takes exactly one argument (0 given)")
#  print("文件已关闭")
# elif f.seek(-10, 2):
#  print("错误信息为can't do nonzero end-relative seeks")
#  print("文件已关闭")
# elif f.close():
#  print("文件已关闭")
# else:
#  print("文件未关闭")

# f = open("src/step1/test.txt", "r")
# try:
#     eval(input())
#     # 补充代码使普通的 open 语句具有 with open 的功能
#     f.close()
# except TypeError:
#           print("错误信息为write() takes exactly one argument (0 given)")
#           f.close()
# except IOError:
#     print("错误信息为can't do nonzero end-relative seeks")
#     f.close()
# ########## End ##########
# if f.closed:
#     print("文件已关闭")
# else:
#     print("文件未关闭")

import os
path=input()

if not os.path.exists(path):
      print("文件不存在")
try:
    f=open(ss,'r')
    print(f.read())
    print("文件存在")
except:
    print("文件存在")