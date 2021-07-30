"""
---- 加强版 ---
创建三个恐怖分子
    三个都要开枪 ，三个对象目前的状态
三个恐怖分子都要死亡
    三个满足同时死亡
三个恐怖分子能够同时开枪
    随机数 ： random
    import random  一定写在所有程序的前面
    random.randint(1,3) 产生1到3的随机数
    产生随机数，判断是几就向几号敌人开枪
"""
import random
class Person:
    def __init__(self,name):
        self.name = name
        self.life = 100
    def __str__(self):
        return "%s当前的生命值为: %d" % (self.name,self.life)

class Hero(Person):
    def fire(self ,p):
        damage = 40
        print("%s向%s开枪，造成了%d伤害" % (self.name,p.name,damage))
        if p.life < damage:
            p.life = 0
        else:
            p.life = p.life - damage
    def __str__(self):
        state = ""
        if self.life == 100:
            state = "无伤"
        elif self.life >= 70 and self.life < 100:
            state = "轻伤"
        elif self.life >= 1 and self.life < 70:
            state = "重伤"
        elif self.life <= 0:
            state = "挂了"
        return "%s当前的状态为：%s" %(self.name,state)
class Is(Person):
    def fire(self,p):
        damage = 1
        print("%s向%s开枪,造成%d伤害"% (self.name,p.name,damage))
        if p.life < damage:
            p.life = 0
        else:
            p.life = p.life - damage

def main():
    h = Hero("英雄")
    is1 = Is("不要命")
    is2 = Is("不怕死")
    is3 = Is("还有谁")
    while True:
        # 产生1到3的随机数
        x = random.randint(1,3)
        if x == 1:
            h.fire(is1)
        if x == 2:
            h.fire(is2)
        if x == 3:
            h.fire(is3)
        is1.fire(h)
        is2.fire(h)
        is3.fire(h)
        print()
        if h.life <= 0:
            print("%s死亡，枪战结束" % h.name)
            break
        # 如果恐怖分子挂了 也去打印提升信息
        if is1.life <= 0:
            print("所有的恐怖分子全部死亡，游戏结束")
            break

main()