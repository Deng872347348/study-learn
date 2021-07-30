import turtle
import random
import time

turtle.pensize(1)  # 设置画笔大小，数值越小画出的线条越细
turtle.delay(1)  # 绘画延迟，单位：毫秒，数值越小绘画速度越快
turtle.hideturtle()  # 隐藏画笔
turtle.setup(800, 800)  # 设置画布大小


def star(x, y, left_angle, edge_len, color='yellow'):
    """
    画一个五角星
    :param x: 起始x坐标
    :param y: 起始y坐标
    :param left_angle: 画笔方向逆时针转动度数
    :param edge_len: 五角星边的长度
    :param color: 五角星颜色
    :return:
    """
    turtle.pencolor(color)  # 五角星边的颜色
    turtle.fillcolor(color)  # 五角星内部填充色
    turtle.speed(0)  # 绘制速度，0代表最快，1-10：数字越大越快

    turtle.pu()  # 抬起画笔
    turtle.goto(x, y)  # 移动到初始位置
    turtle.pd()  # 放下画笔

    turtle.begin_fill()  # 开始填充图形
    turtle.left(left_angle)  # 画笔方向以水平方向为基准逆时针转动 left_angle 度
    for _ in range(5):  # 循环绘制 5 条边
        turtle.forward(edge_len)  # 向当前画笔方向移动 edge_len 像素长度，即：绘制五角星的一条边
        turtle.right(144)  # 画笔方向顺时针旋转 180 度，由于五角星内角是36度，所以需要旋转180-36=144度
    turtle.end_fill()  # 填充完成
    turtle.left(-left_angle)  # 将画笔方向恢复为水平方向，以免影响后续画图


# 绘制满天星
turtle.bgpic('./bg.gif')
for _ in range(200):  # 绘制 100 颗星星
    # 随机生成起始坐标、画笔方向和五角星边长
    rand_x = random.randint(-400, 400)
    rand_y = random.randint(0, 400)
    edge_len = random.randint(3, 8)
    left_angle = random.randint(0, 180)
    star(rand_x, rand_y, left_angle, edge_len, '#B7C5D2')

time.sleep(1)

# 绘制五星红旗
turtle.clear()  # 清空之前图形
turtle.bgpic('./red_bg.gif')

star(-360, 320, 0, 80)
star(-260, 350, 40, 18)
star(-235, 330, 20, 18)
star(-235, 295, 0, 18)
star(-260, 270, -10, 18)

turtle.done()