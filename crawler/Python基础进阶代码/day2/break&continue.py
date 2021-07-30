# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# for i in range(1,6): #  L2
#     print(f"----------{i}层---------")
#
#     for j in range(1,9): # 5
#         if i == 3: # L3， 跳过
#             print("-")
#             continue # 跳过本次循环，进入下一次
#         print(f"L{i}-{i}0{j}室")


# 当走到第3层的时候 ，小循环，执行了么？ 如果执行了，执行了几次？

for i in range(1,6): #  L2
    print(f"----------{i}层---------")
    if i == 3:  # L3， 跳过
        print("-3层不走...")
        continue # 跳过本次循环，进入下一次
    for j in range(1,9): # 5
        if i == 4 and j == 4:
            print("遇到鬼屋404房间，over 了....")
            break  # 结束当前循环
        print(f"L{i}-{i}0{j}室")
