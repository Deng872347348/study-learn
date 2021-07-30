# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

black_gf_age = 24

for i in range(3):
    guess = int(input("猜猜黑姑娘多大了>>:"))
    if guess > black_gf_age:
        print("猜的太大了，往小里试试...")
    elif guess < black_gf_age:
        print("猜的太小了，往大里试试...")
    else:
        exit("恭喜你，猜对了...")  # 退出程序
