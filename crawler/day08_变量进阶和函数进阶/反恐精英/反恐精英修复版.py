"""
--------修复版 ----
修复英雄的信息显示模式
状态描述 ： 0 - 1 - 70 - 99 -100  挂了 轻伤 重伤 无伤
            if ... eifi .... and组合

修复生命值为负的问题
  射击时如果生命值<伤害值，生命值 = 0 否则正常减生命值
"""

class Person:
    def __init__(self,name):
        self.name = name
        self.life = 100
    def __str__(self):
        return "%s当前的生命值为：%d" % (self.name,self.life)
class Hero(Person):
    # 射击所造成的伤害
    def fire(self,p):
        dammage = 40
        print("%s向%s开枪，造成了%d伤害" %(self.name,p.name,dammage))
        p.life = p.life - dammage
        if p.life < dammage:
            p.life = 0
        else:
            p.life = p.life - dammage  # 从 100 到 1 正常扣除血量
    def __str__(self):
        state = ""   # return 会根据当前所造成的伤害判断目前的状态
        if self.life  == 100:
            state = "无伤"
        elif self.life >= 70 and self.life < 100:
            state = "轻伤"
        elif self.life >= 1 and self.life < 70:
            state = "重伤"
        elif self.life <= 0:
            state = "挂了"
        return "%s当前的状态为：%s"%(self.name,state)

class Is(Person):
    # 射击所造成的伤害
    def fire(self,p):
        dammage = 10
        print("%s向%s开枪，造成了%d伤害" %(self.name,p.name,dammage))
        p.life = p.life - dammage

def main():   # 一切程序运行开端
    # 创建英雄和敌人对象
    h = Hero("【英雄】")
    is1 = Is("【敌人】")
    # 重复开枪 哪一方倒下就结束游戏
    while True:
        h.fire(is1)
        is1.fire(h)
        print(h)
        print(is1)
        print()
        # 设置游戏结束条件
        # 12.如果英雄挂了 打印提示信息 循环退出
        if h.life <= 0:
            print("%s死亡，枪战结束"% h.name)
            break
        # 如果恐怖分子挂了 也去打印提升信息
        if is1.life <= 0:
            print("所有的恐怖分子全部死亡，游戏结束")
            break
# main函数 就是程序的主入口
# 定义main函数
main()