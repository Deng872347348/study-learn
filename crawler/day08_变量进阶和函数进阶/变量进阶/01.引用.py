def test(num):
    print("在函数的内部 %d 对应的地址是 %d"% (num, id(num)))
    # print(type())
    # 定义一个字符串的变量
    result = 'hello'

    print("函数要返回的数据的内存地址是 %d"% id(result))
    return result
# 数据的保存地址本质上就是一个数字
    # 定义一个数字的变量
a = 10
print("a 变量保存数据的内存地址是 %d " % id(a))
# 调用 test 函数 ，本质上传递的实参保存数据的引用，而不是实参所保存的数据
# 如果说函数有返回值，但是没有定义变量去接收
# 程序不会报错，但是无法获得返回的结果
r = test(a)
print("%s 变量保存数据的内存地址是 %d " % (r,id(r)))