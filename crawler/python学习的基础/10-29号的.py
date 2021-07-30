# imgsrc="/img10.360buyimg.com/seckillcms/5f805563E6481610c/aa5d10d24da.png"
#
# list=imgsrc.split("/")
# print(list)
# list1=list[4]
# list2=list1.split(".")
# print(list2[0])
# s = input('请输入一个字符串：')
# if not s:
#     print('请不要输入空字符串！')
#     s = input('请重新输入一个字符串：')
#
# a = len(s)
# i = 0
# count = 1
# while i <= (a/2):
#     if s[i] == s[a-i-1]:
#         count = 1
#         i += 1
#     else:
#         count = 0
#         break
#
# if count == 1:
#     print('您所输入的字符串是回文')
# else:
#     print('您所输入的字符串不是回文')
# list=str(input())
# if list.startswith("130"):
#  print("中国联通")
# elif list.startswith("133"):
#  print("中国电信")
# elif list.startswith("134"):
#  print("中国移动")
# else:
#       print()
# code=input()
# list=code[len(code)-4::]
# list4=code[0:len(code)-4]
#
# list1=list.rjust(5," ")
#
# list2=list4+list1
#
# print(list2)
str = "     this is string example....wow!!!     ";
print (str.lstrip());
str = "88888888this is string example....wow!!!8888888";
print (str.lstrip('8'));