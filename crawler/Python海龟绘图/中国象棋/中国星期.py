import turtle             #  导入turtle库函数，重中之重
# 自定义画布面板大小和顶点位置
#  定义画布大小和顶点位置
turtle.setup(width=800, height=880, startx=600, starty=0)
turtle.screensize(300, 300, "white")    # 这是棋盘的宽和高，还有背景颜色设置

#自定义画笔的各种设置
s = turtle.Pen()           #  为了后面函数调用的各种烦杂设置，采用定义变量设置画笔，等同于赋值变量
s.speed(6)  # 移动速度
s.pencolor()  # 颜色
s.pensize(1.5)  # 宽度

# 画横线
s.penup()  # 抬起
s.goto(-240, 270)  # 起始点
s.pendown()  # 下笔
for i in range(1, 6, 1):
    s.forward(480)  # 画480px
    s.penup()  # 抬起
    s.right(90)  # 右转90度
    s.forward(60)  # 移动60px
    s.right(90)  # 右转90度
    s.pendown()  # 下笔
    s.forward(480)  # 画480px
    s.penup()  # 抬起
    s.left(90)  # 左转90度
    s.forward(60)  # 移动60px
    s.left(90)  # 左转90度
    s.pendown()  # 下笔

# 画竖线
s.left(90)
s.penup()
s.forward(60)
s.pendown()
for i in range(1, 5, 1):
    s.forward(240)
    s.penup()
    s.forward(60)
    s.pendown()
    s.forward(240)
    s.right(90)
    s.forward(60)
    s.right(90)
    s.forward(240)
    s.penup()
    s.forward(60)
    s.pendown()
    s.forward(240)
    s.left(90)
    s.forward(60)
    s.left(90)
s.forward(540)

# 画斜线
s.left(90)
s.forward(480)
s.left(90)
s.forward(540)
s.left(90)
s.forward(180)
s.left(45)
s.forward(120 * 1.414)
s.left(45)
s.forward(-120)
s.left(45)
s.forward(120 * 1.414)
s.penup()
s.goto(-60, 270)
s.pendown()
s.right(180)
s.forward(120 * 1.414)
s.right(45)
s.forward(-120)
s.right(45)
s.forward(120 * 1.414)
# 调用函数
def apple(x, y):
    s.penup()
    s.goto(x + 5, y + 5)
    s.pendown()
    s.setheading(0)  # 设置当前角度朝向
    s.forward(5)
    s.goto(x + 5, y + 5)
    s.left(90)
    s.forward(5)
    s.penup()
    s.goto(x + 5, y - 5)
    s.pendown()
    s.setheading(0)
    s.forward(5)
    s.goto(x + 5, y - 5)
    s.left(90)
    s.forward(-5)
    s.penup()
    s.goto(x - 5, y + 5)
    s.pendown()
    s.setheading(0)
    s.forward(-5)
    s.goto(x - 5, y + 5)
    s.left(90)
    s.forward(5)
    s.penup()
    s.goto(x - 5, y - 5)
    s.pendown()
    s.setheading(0)
    s.forward(-5)
    s.goto(x - 5, y - 5)
    s.left(90)
    s.forward(-5)


def p(x, y):
    s.penup()
    s.goto(x - 5, y + 5)
    s.pendown()
    s.setheading(0)
    s.forward(-5)
    s.goto(x - 5, y + 5)
    s.left(90)
    s.forward(5)
    s.penup()
    s.goto(x - 5, y - 5)
    s.pendown()
    s.setheading(0)
    s.forward(-5)
    s.goto(x - 5, y - 5)
    s.left(90)
    s.forward(-5)


def w(x, y):
    s.penup()
    s.goto(x + 5, y + 5)
    s.pendown()
    s.setheading(0)
    s.forward(5)
    s.goto(x + 5, y + 5)
    s.left(90)
    s.forward(5)
    s.penup()
    s.goto(x + 5, y - 5)
    s.pendown()
    s.setheading(0)
    s.forward(5)
    s.goto(x + 5, y - 5)
    s.left(90)
    s.forward(-5)
    s.penup()

# 修饰炮和兵所在点
apple(180, 150)
apple(-180, 150)
apple(180, -150)
apple(-180, -150)
apple(-120, 90)
apple(0, 90)
apple(120, 90)
apple(-120, -90)
apple(0, -90)
apple(120, -90)

p(240, 90)
p(240, -90)
w(-240, -90)
w(-240, 90)

# 绘制一个长方形外围线，设置笔的粗细
s.penup()
s.goto(-250, -280)
s.pendown()
s.pensize(8)
s.forward(560)
s.right(90)
s.forward(500)
s.right(90)
s.forward(560)
s.right(90)
s.forward(500)
s.right(90)

turtle.done()                #终止画笔，但可视化窗口不闪退
