import turtle as t
import  random
import  time

t.pensize(1)#设置画笔的大小

t.delay(1) #绘画延池，数组越小绘画越快
t.hideturtle() #隐藏画笔

t.screensize(800,800) #数组画布大小及颜色

#绘制一个五角星
#封装一个函数用来绘制满天星
def stars(x,y,left_angle,edge_len,color='yellow'):#设置五角星起始的x,y值，五角星逆时针以及度数
    #param  x:起始坐标
    #param y:起始y坐标
    #param left_angle:画笔方向逆时针转动度数
    #param edge_len:五角星边的长度
    #param color:五角星颜色
    #五角星边的颜色
    t.pencolor(color)
    #五角星内部填充颜色
    t.fillcolor(color)
    #绘制速度，0代表最快，1-10：数字越大越快
    t.speed(0)
    t.pu() #抬起画笔
    t.goto(x,y) #移动到初始位置
    t.pd()#放下画笔
    t.begin_fill()#开始填充颜色
    #画笔方向以水平方向为基准
    #逆时针转动 left_angel 度
    t.left(left_angle)
    #循环绘制五角星的5条边
    for _ in range(5):
        t.forward(edge_len)
        t.right(144)
    t.end_fill()#填充完成
    #将画笔方向恢复为水平方向，以免影响后续画图

t.done()
#     t.pencolor('yellow') #设置画笔的颜色
#     t.fillcolor('yellow') #设置填充的颜色
#     t.speed(0)#绘画的速度
#     t.penup()#抬起画笔
#     t.goto(x,y)#移动到起始的位置
#     t.begin_fill()#开始填充颜色
#     t.pendown()#落下画笔
#     t.left(left_angle)#逆时针转动
#     for i in range(5):
#         t.forward(edge_len)#画一条直线
#         t.right(144) #顺时针旋转144度
#     t.end_fill() #结束填充
#     t.left(-left_angle)#将画笔回归至水平方向
# t.done()
# #重复绘制五角星
# for _ in range(300): #绘制300颗星星
#     x=random.randint(-450,450)#在450到450之间随机移动x的起始位置
#     y=random.randint(0,400) #在0到400之间随机移动y的起始位置
#     edge_len=random.randint(3,8) #在3到8之间随机选取长度
#     left_angle=random.randint(0,180)#在0到180之间随机逆时针旋转
#     stars(x,y,left_angle,edge_len)
# t.exitonclick()

