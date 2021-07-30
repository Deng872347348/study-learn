import random
class Person:
    def __init__(self,name):
        self.name = name
        self.life = 100
    def __str__(self):
        return "%s当前的生命值为：%d" %(self.name,self.life)
class Hero(Person):
    def fire(self ,p):
        # 加入命中率
        hit = random.randint(1,100)
        if hit > 20 :   #命中率80%
            # 判断当前射击的对象是否是尸体
            if p.life == 0 :
                print("%s都死了，就不要鞭尸了" % p.name)
            else:
                damage = random.randint(20, 50)
                print("%s向%s开枪，造成了%d伤害" % (self.name, p.name, damage))
                if p.life < damage:
                    p.life = 0
                else:
                    p.life = p.life - damage
        else:
            print("枪法真臭，这是个臭籽，没有打到恐怖份子")

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
    def fire(self, p):
        damage = random.randint(5,15)
        hit = random.randint(1,100)
        if hit > 80 :
            print("%s向%s开枪，造成了%d伤害" % (self.name, p.name, damage))
            if p.life < damage:
                p.life = 0
            else:
                p.life = p.life - damage
        else :
            print("%s枪法不行啊，回去接着练吧" % self.name)

def main():
    h = Hero("【英雄】")
    is1 = Is("【不要命】")
    is2 = Is("【不怕死】")
    is3 = Is("【还有谁】")
    while True:
        # 产生1到3的随机数
        x = random.randint(1,3)
        if x == 1:
            h.fire(is1)
        elif x == 2:
            h.fire(is2)
        else:
            h.fire(is3)
        is1.fire(h)
        is2.fire(h)
        is3.fire(h)
        print(h)
        print(is1)
        print(is2)
        print(is3)
        print()
        #设置结束条件
        if h.life <= 0:
            print("%s死亡，枪战结束" % h.name)
            break
        if is1.life <= 0 and is2.life <= 0 and is3.life <= 0:
            print("所有恐怖份子全部死亡，枪战结束")
            break
main()
