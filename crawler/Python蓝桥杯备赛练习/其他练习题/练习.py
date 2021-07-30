# 从1到2020中这些数字中有多少个2（注意：不是问多少个数字里有2）
# mw=0
# for i in range(1,2021):
#     mw+=str(i).count('2')
# print(mw)

#特色回文数
# while True:
#     try:
#
#         n = int(input())
#         for i in range(10000, 1000000):
#             a = str(i)
#             b = 0
#             if a == a[::-1]:  # 这里的a[::-1]表示把字符串a倒序
#                 for j in a:
#                     b += int(j)
#                 if b == n:
#                     print(a)
#     except:
#         break
