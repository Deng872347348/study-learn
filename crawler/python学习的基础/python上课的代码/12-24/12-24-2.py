class Fruit:
    def __init__(self,color="绿色"):
        Fruit.color=color
    def harvest(self):
        print("水果原来是:"+Fruit.color+"的！")
class Apple(Fruit):
    def __init__(self):
        print("我是苹果")
        super().__init__()
apple=Apple()
apple.harvest()

