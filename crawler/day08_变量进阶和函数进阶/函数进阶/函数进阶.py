def measure():
    """返回当前的温度"""
    print("开始测量....")
    temp = 39
    wentness = 10
    print("测试结束")

# 在利用元祖返回的时候，如果函数是返回的元祖，括号可以省略
    return temp,wentness

# result = temp,wetness = measure()
result = measure()
print(result)