num = 10

def demo1():

    # 希望修改全局变量的值 - 使用global 声明一下变量即可
    global num

    num = 99
    print("demo1 ==> %d " % num)

def demo2():
    print("demo2 ==> %d" % num)

demo1()
demo2()