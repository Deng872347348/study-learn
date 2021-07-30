# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

import random
import string


car_num_sample = string.digits+string.ascii_uppercase

print(random.sample(car_num_sample,5))

count = 3
while count > 0 :
    count -= 1
    num_list = []
    for i in range(20):
        second_letter = random.choice(string.ascii_uppercase)
        car_num = f"京{second_letter}-{ ''.join(random.sample(car_num_sample,5)) }"
        num_list.append(car_num)
        print(i, car_num)

    choice = input("choice:").strip()
    if choice in num_list:
        exit(f"恭喜你选购成功，您的新车牌是{choice}")
    else:
        print(f"未选中， 还有{count}次机会")

