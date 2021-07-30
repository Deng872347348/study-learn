#定义父类
class Fruit(object):
    color="绿色"
    def harverst(self,color):
        print("水果是"+color+"颜色")
        print("水果已经收获了...")
        print("水果原来的颜色是"+Fruit.color)
class Apple(Fruit):
    color="红色"
    def __init__(self):
        print("这是苹果")
class Orange(Fruit):
    color="黄色"
    def __init__(self):
        print("这是橘子")
apple=Apple()
apple.harverst(Apple.color)
orange=Orange()
orange.harverst(Orange.color)


# 第三步：按照预期输出打印结果
# print("Dog {}的年龄为{}岁".format(a.name, a.age))
# 私有属性的访问上，在类里面提供getxxx(),返回私有属性
# 私有属性的访问2.通过对象名，类名+私有属性名（不提倡）
