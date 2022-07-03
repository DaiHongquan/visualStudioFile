import turtle
import time


def curvemove():
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)
#turtle.speed(100)
#turtle.delay(1)
#turtle.tracer(n=1, delay=0)
#不展示绘图过程
#turtle.tracer(False)
turtle.bgcolor("black")
turtle.color('red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()
turtle.write('琪宝~生日快乐',  font = ('SimHei', 15, 'bold'))
turtle.hideturtle()
time.sleep(3)