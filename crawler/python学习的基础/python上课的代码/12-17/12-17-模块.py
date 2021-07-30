class Animal:
    #构造方法，要求第一个参数一定是self，self表示
    def __init__(self,foot,weight,height):
        self.foot=foot
        self.weight=weight
        self.height=height
        print("我是构造方法")

        #定义类中方法
    def printstr(self):
        print("腿的数量："+str(self.foot)+"体重是:"+str(self.height)+"身高是："+str(self.weight))
animall=Animal(2,30,50)
animall.printstr()
#在类的外面访问类属性：类名.类属性或者对象名




