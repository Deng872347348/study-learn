# def func():
#     return i
#
# data_list = [ func  for i in range(10) ]


data_list = [lambda: i for i in range(10)]

print(data_list)  # [函数,函数,函数]    i=9

v1 = data_list[0]()  # 9
v2 = data_list[6]()  # 9
