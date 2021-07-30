# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

black_girl_age = 26

guess = int(input("输入你的猜测:"))

if guess > black_girl_age:  # 猜大了
    print("你讨厌，人家哪有这么老啊。。。。")
elif guess < black_girl_age: # 猜小了
    print("真开心，但实际我比这个岁数要大呢...")
else:
    print("恭喜你，猜对了，可以今天把我领回家了。。。。")

