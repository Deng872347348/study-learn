# 1.减少判断的代码


def func1():
    pass


def func2():
    pass


def func3():
    pass


func_list = [func1, func2, func3]

for item in func_list:
    result = item()
    if result:
        break
    

# 连续执行这三个函数，
#  - 如果func1返回True，后面的函数就不再执行；
#  - 如果func2返回True，后面的函数就不再执行；
#  - 如果func3返回True
# v1 = func1()
# if v1:
#     result = v1
# else:
#     v2 = func2()
#     if v1:
#         result = v2
#
# func3()
