import  turtle as t
t.speed(0)
def circle(x,y,r,color):
  t.goto(x,y)
  t.color(color,color)
  t.begin_fill()
  t.circle(r)
  t.end_fill()
circle(0,-200,200,'red')
circle(0,-150,150,'white')
circle(0,-100,100,'red')
circle(0,-50,50,'blue')


def wjx(x,y,p,color):
    t.goto(x,y)
    t.color(color,color)
    t.begin_fill()
    for i in range(5):
            t.forward(p)
            t.right(144)
    t.end_fill()

if __name__=="__main__":
  wjx(-48,15,93,'white')
  t.done()



