import pygame
from sys import exit
from random import randint

#开发函数
from  math import  sqrt

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

#球类
class Ball:
    """球类"""
    all_ball=[]
    def __init__(self,x=0,y=0,radius=0,color=(255,0,0)):
        self.x=x
        self.y=y
        self.x_seed=0
        self.y_seed=0
        self.radius=radius
        self.color=color
    def move(self):
        self.x+=self.x_seed
        self.y+=self.y_seed
        if self.x<self.radius or self.x>SCREEN_WIDTH - self.radius:
            self.x_seed= - self.x_seed

        if self.y<self.radius or self.y>SCREEN_HEIGHT - self.radius:
            self.y_seed= - self.y_seed
    """判断当前的小球是否和另外的一个小球相撞"""
    def crash(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        distance=sqrt(dx**2+dy**2)
        if distance<self.radius+other.radius:
            value=randint(0,1)
            if value==0:
                #继承被吃的球半径
                self.radius+=int(other.radius*0.4)
                #让被吃球消失
                Ball.all_ball.remove(other)
            else:
                other.radius+=int(self.radius*0.4)
                Ball.all_ball.remove(self)
#颜色类
class Color:
    """颜色类"""
    RED=(255,0,0)
    GREEN=(0,255,0)
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    GRAY=(100,100,100)

    @staticmethod
    def rand_color():
        return  randint(0,255),randint(0,255),randint(0,255)

    #============game_loop========
def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("小球碰撞")

        while True:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #鼠标点击需要产生一个球
                     born_ball(event.pos)
        pygame.time.delay(50)
        #将球渲染到界面上(刷新界面)
        show_ball(screen)

        #让小球都动起来
        move_all_ball()

        #去检测界面的球的碰撞
        all_ball_crash()
"""球的碰撞检测"""

def all_ball_crash():
    #先拿出一个球
    for ball in Ball.all_ball:
        #拿另外一个球，不能事第一个
        for ball2 in Ball.all_ball:
            ball.crash(ball2)
#球动起来

def move_all_ball():
    for ball in Ball.all_ball:
        ball.move()

#将球画到指定的位置， place:地方

def show_ball(place):
    #清屏
    place.fill(Color.WHITE)
    #画球
    for ball in Ball.all_ball:
        pygame.draw.circle(place,ball.color,(ball.x,ball.y),ball.radius)
    pygame.display.flip()

#在指定位置产生一个球
def born_ball(pos):
    x,y=pos
    r=randint(5,15)#随机产生球的半径
    ball_color=Color.rand_color() #随机产生球的颜色

    #创建了对应的球
    ball=Ball(x,y,r,ball_color)
    ball.x_seed=randint(-8,8)
    ball.y_seed=randint(-8,8)
    #将球保存起来
    Ball.all_ball.append(ball)
if __name__ == '__main__':
    main()