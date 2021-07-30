import turtle
t=turtle.Pen()
#正方形
# t.reset()
# for i in range(1,5):
#     t.forward(50)
#     t.left(90)
#
# turtle.done()

#画星星
# t.reset()
# for i in range(1,9):
#     t.forward(100)
#     t.left(225)
# turtle.done()

#画一个圆刺
# t.reset()
# for i in range(1,38):
#     t.forward(100)
#     t.left(175)
# turtle.done()
#画螺旋星
# t.reset()
# for i in range(1,20):
#     t.forward(100)
#     t.left(95)
# turtle.done()


#画一个星星
# t.reset()
# for x in range(1,19):
#     t.forward(100)
#     if x%2==0:
#      t.left(175)
#     else:
#       t.left(225)
# turtle.done()

t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
#车身
t.color(0,0,0)
t.up()
t.forward(10)
t.down
t.begin_fill()
t.circle(10)
t.end_fill()
#左车轮
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down
t.circle(10)
t.end_fill()
#右车轮
t.up()
t.forward(180)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down
t.circle(10)
t.end_fill()

turtle.done()

