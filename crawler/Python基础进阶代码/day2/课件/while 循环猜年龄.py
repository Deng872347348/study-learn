# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城


black_gf_age = 25
count = 0
while True:
    count += 1
    if count <= 3:
        guess = int(input("猜猜黑姑娘多大了>>:"))
        if guess > black_gf_age:
            print("猜的太大了，往小里试试...")
        elif guess < black_gf_age:
            print("猜的太小了，往大里试试...")
        else:
            exit("恭喜你，猜对了...")  # 退出程序
    else:
        choice = input("猜了3次还不对，真是笨呀，还玩么? [y/Y or n/N]").strip()
        if len(choice) == 0 : continue # 不能写空值
        if choice in ("y","Y"):
            count = 0
        elif choice in ("n","N"):
            exit("bye.")
        else:
            print("请输入正确的选项...")


