#导入海龟绘图库
import turtle as t

# #设置画布属性 宽高背景颜色，如果画布大于窗体，窗体会出现滚动条，默认400,300,none
# turtle.screensize(canvwidth=None,canvheight=None,bg=None)
# #设置窗口大小 startx starty 0,0左上角开始，None中心开始
# turtle.setup(width=0.5,height=0.75,startx=None,starty=None)
# #设置画笔属性
# turtle.pensize(2)
# turtle.pencolor('red')#设置画笔颜色
# turtle.fillcolor('yellow')#可以是字符串或者rgb
# turtle.speed(5)#1~10数字越大越快
# #提笔、移动、落笔
# turtle.penup()#提笔，不会绘制
# turtle.pendown()#落笔，开始绘制
# #绘制线条
# turtle.left(degree)向左多少度
# turtle.right(degree)#向右多少度
# turtle.forward(distince)#向前
# turtle.backward(distince)#向后
# turtle.goto(x,y)#将画笔移动至x，y
# turtle.circle(r,degree)#画圆，半径为正(负)表示圆心在画笔左边（右边）,r半径，degree绘制多少，360为整个圆
# turtle.setx()#将当前x轴移动到指定位置
# turtle.sety()#将当前y轴移动到指定位置
# turtle.setheading(angle)/turtle.seth(angle)#设置当前朝向为angle角度
# home()#设置当前画笔为原点，朝向东
# dot(r)#绘制一个指定直径和颜色的圆点
# #绘制标志
# turtle.fillcolor('yellow')#填充颜色
# turtle.color(color1,color2)#同时设置pencolor、fillcolor
# turtle.filling()#返回当前是否在填充状态
# turtle.begin_fill()#准备开始填充
# turtle.end_fill()#填充完成
# turtle.hideturtle()#隐藏画笔的turtle形状
# turtle.showturtle()#显示画笔的turtle形状
# # #绘图完成保留窗口
# # turtle.done()
# #全局控制
# turtle.clear()#清空turtle窗口但是turtle位置和状态不变
# turtle.reset()#清空窗口，重置turtle为起始状态
# turtle.undo()#撤销上一个turtle动作
# turtle.isvisible()#返回当前turtle是否可见
# turtle.stamp()#复制当前图形
# turtle.write(s,[,font='font-name',font_size,'font_type'])#写文本，s为文本内容，font是字体参数，分别为字体名称，大小和类型，font是可选项
# #其他命令
# turtle.mainloop()#启动循环事件-调用Tkinter的mainloop函数
# turtle.done()#绘图完成保留窗口，必须是海龟图形程序中的最后一个语句
# turtle.delay(delay=None)#设置或返回以毫秒为单位的绘图延迟
# turtle.begin_poly()#开始记录多边形的顶点。当前的海龟位置是多边形的一个顶点
# turtle.end_poly()#停止记录。当前的海龟位置是多边形的最后一个顶点。将与第一个顶点相连
# turtle.get_poly()#返回最后记录的多边形
# turtle.mode(mode=None)#设置海龟模式（'standard','logo'或'world'）并执行重置。如果没有给出模式，则返回当前模式
# turtle.tracer(True/False)#打开关闭海龟动画
# turtle.ontimer(x,y)#在y毫秒后继续调用x方法


transformX = 100
transformY = -100

def gotoTransform(x,y):
    t.goto(x + transformX,y + transformY)
##绘制小猪佩奇
t.screensize(400,300)
t.pensize(4)
#t.colormode(255)#设置gbk颜色范围为0-255
t.color('#FF9BC0','pink')
t.setup(840,500)
t.speed(10)

#画鼻子
def nose():
    t.up()
    gotoTransform(-100,100)
    t.down()
    t.seth(-30)
    t.begin_fill()
    a = 0.4#初始步长
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    t.up()
    t.seth(90)
    t.fd(25)
    t.seth(0)
    t.fd(10)
    t.down()
    t.pencolor('#FF9BC0')
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color('#A0522D')
    t.end_fill()
    t.up()
    t.seth(0)
    t.fd(20)
    t.down()
    t.pencolor('#FF9BC0')
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color('#A0522D')
    t.end_fill()

def head():
    t.color(('#FF9BC0'),'pink')
    t.up()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.fd(0)
    t.down()
    t.begin_fill()
    t.seth(180)
    t.circle(300,-30)
    t.circle(100,-60)
    t.circle(80,-100)
    t.circle(150,-20)
    t.circle(60,-95)
    t.seth(161)
    t.circle(-300,15)
    t.up()
    gotoTransform(-100,100)
    t.down()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
#画耳朵
def ears():
    t.color(('#FF9BC0'),'pink')
    t.up()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.down()
    t.begin_fill()
    t.seth(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,54)
    t.end_fill()
    t.up()
    t.seth(90)
    t.fd(-12)
    t.seth(0)
    t.fd(30)
    t.down()
    t.begin_fill()
    t.seth(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,56)
    t.end_fill()
#画眼睛
def eyes():
    t.color(('#FF9BC0'),'white')
    t.up()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-95)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color('black')
    t.up()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.down()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color(('#FF9BC0'),'white')
    t.up()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color('black')
    t.up()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.down()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
#画腮
def cheek():
    t.color(('#FF9BC0'))
    t.up()
    t.seth(90)
    t.fd(-95)
    t.seth(0)
    t.fd(65)
    t.down()
    t.begin_fill()
    t.circle(30)
    t.end_fill()
#画嘴
def mouth():
    t.color('#EF4513')
    t.up()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(-100)
    t.down()
    t.seth(-80)
    t.circle(30,40)
    t.circle(40,80)
#画身体
def body():
    t.color('red',('#FF6347'))
    t.up()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-78)
    t.down()
    t.begin_fill()
    t.seth(-130)
    t.circle(100,10)
    t.circle(300,30)
    t.seth(0)
    t.fd(0)
    t.fd(230)
    t.seth(90)
    t.circle(300,30)
    t.circle(100,3)
    t.color(('#FF9BC0'),('#FF6464'))
    t.seth(-135)
    t.circle(-80,63)
    t.circle(-150,24)
    t.end_fill()
#画手
def hand():
    t.color(('#FF9BC0'))
    t.up()
    t.seth(90)
    t.fd(-40)
    t.seth(0)
    t.fd(-27)
    t.down()
    t.seth(-160)
    t.circle(300,15)
    t.up()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(0)
    t.down()
    t.seth(-10)
    t.circle(-20,90)
    t.up()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(237)
    t.down()
    t.seth(-20)
    t.circle(-300,15)
    t.up()
    t.seth(90)
    t.fd(20)
    t.seth(0)
    t.fd(20)
    t.seth(0)
    t.fd(0)
    t.down()
    t.seth(-170)
    t.circle(20,90)
#画脚 
def foot():
    t.pensize(10)
    t.color(('#F08080'))
    t.up()
    t.seth(90)
    t.fd(-75)
    t.seth(0)
    t.fd(-180)
    t.down()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color('black')
    t.pensize(15)
    t.fd(20)
    t.pensize(10)
    t.color(('#F08080'))
    t.up()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.down()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color('black')
    t.pensize(15)
    t.fd(20)
#画尾巴
def tail():
    t.pensize(4)
    t.color(('#FF9BC0'))
    t.up()
    t.seth(90)
    t.fd(70)
    t.seth(0)
    t.fd(75)
    t.down()
    t.seth(0)
    t.circle(70,20)
    t.circle(10,330)
    t.circle(70,30)

def main():
    t.tracer(False)
    nose() 
    head() 
    ears() 
    eyes() 
    cheek() 
    mouth() 
    body() 
    hand() 
    foot() 
    #t.tracer(True)
    tail()


