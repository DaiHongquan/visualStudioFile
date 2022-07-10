#导入海龟绘图库
import turtle as t
import time
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


transformX = -350
transformY = -100

def gotoTransform(x,y):
    t.goto(x + transformX,y + transformY)
##绘制眨眼皮卡丘
#准备设置
t.screensize(400,300)
t.pensize(3)
t.setup(840,500)
t.speed(10)
t.up()
t.backward(200)
t.down()



#画左偏曲线函数
def radian_left(angle,distance,step,n):
    for i in range(n):
        distance += step
        t.left(angle)
        t.fd(distance)
#画右偏曲线函数
def radian_right(angle,distance,step,n):
    for i in range(n):
        distance += step
        t.right(angle)
        t.fd(distance)
#画耳朵
def initEars():
    #左耳朵
    t.color('black','yellow')
    t.up()
    gotoTransform(-50,100)
    t.down()
    t.seth(70)
    t.begin_fill()
    radian_left(1.5,2,0.1,32)
    t.seth(235)
    radian_left(1.5,2,0.1,35)
    t.seth(30)
    t.fd(28)
    t.end_fill()
    #黑左耳朵尖
    t.up()
    gotoTransform(-50,175)
    t.down()
    t.seth(110)
    t.begin_fill()
    t.fillcolor('black')
    radian_left(0.5,2,0.1,15)
    t.seth(245)
    radian_left(0.5,2,0.1,15)
    t.seth(5)
    t.fd(20)
    t.end_fill()
    #右耳朵
    t.color('black','yellow')
    t.up()
    gotoTransform(50,100)
    t.down()
    t.seth(45)
    t.begin_fill()
    radian_right(1.5,2,0.1,35)
    t.seth(230)
    radian_right(1.5,2,0.1,33)
    t.seth(145)
    t.fd(18)
    t.end_fill()
    #黑右耳朵尖
    t.fillcolor('black')
    t.up()
    gotoTransform(135,131)
    t.down()
    t.seth(13)
    t.begin_fill()
    radian_right(2,2,0.1,14)
    t.seth(230)
    radian_right(2,2,0.1,10)
    t.seth(130)
    t.fd(25)
    t.end_fill()
#画脚
def initFoots():
    t.fillcolor('yellow')
    t.up()
    gotoTransform(-65,-200)
    t.down()
    t.begin_fill()
    t.seth(225)
    radian_left(0.5,1.2,0,12)
    radian_left(35,0.6,0,4)
    radian_left(1,1.2,0,18)
    t.seth(160)
    t.fd(13)
    t.end_fill()
    t.up()
    gotoTransform(65,-200)
    t.down()
    t.seth(315)
    t.begin_fill()
    radian_right(0.5,1.2,0,12)
    radian_right(35,0.6,0,4)
    radian_right(1,1.2,0,18)
    t.seth(20)
    t.fd(13)
    t.end_fill()
   
#画身体
def initBody():
    t.up()
    gotoTransform(95,25)
    t.down()
    t.seth(90)
    t.begin_fill()
    t.circle(95,180)
    t.seth(260)
    radian_left(0.5,1,0,35)
    radian_left(2,1.8,0,35)
    t.seth(255)
    radian_left(0.4,2,0.2,27)
    radian_left(2.8,1,0,45)
    radian_right(0.9,1.45,0,31)
    t.seth(355)
    radian_right(0.9,1.45,0,31)
    radian_left(2.8,1,0,45)
    radian_left(0.4,2,0.2,27)
    t.seth(9)
    radian_left(2,1.8,0,35)
    radian_left(0.5,1,0,36)
    t.end_fill()
#画脸
def initFace():
    t.fillcolor('red')
    t.up()
    gotoTransform(-63,10)
    t.down()
    t.seth(90)
    t.begin_fill()
    t.circle(10,360)
    t.end_fill()
    t.fillcolor('red')
    t.up()
    gotoTransform(63,-10)
    t.down()
    t.seth(-90)
    t.begin_fill()
    t.circle(10,360)
    t.end_fill()
    t.up()
    gotoTransform(0,0)
    t.down()
    t.seth(235)
    radian_right(5,0.8,0,30)
    t.up()
    gotoTransform(0,0)
    t.down()
    t.seth(305)
    radian_left(5,0.8,0,30)
#画手
def initHands():
    t.up()
    gotoTransform(-45,-100)
    t.down()
    t.seth(285)
    radian_right(0.4,1.2,0,26)
    radian_right(5,0.35,0,26)
    radian_right(0.3,1.2,0,15)
    t.up()
    gotoTransform(45,-100)
    t.down()
    t.seth(255)
    radian_left(0.4,1.2,0,26)
    radian_left(5,0.35,0,26)
    radian_left(0.3,1.2,0,15)
#画眼睛
def initEyes():
    #左眼
    t.fillcolor('black')
    t.up()
    gotoTransform(-45,20)
    t.down()
    t.seth(90)
    t.begin_fill()
    #t.circle(8,360)
    t.seth(0)
    t.fd(10)
    t.end_fill()
    #右眼
    t.fillcolor('black')
    t.up()
    gotoTransform(45,20)
    t.down()
    t.seth(-90)
    t.begin_fill()
    t.circle(10,360)
    t.end_fill()
#画闭眼
def closeEyes():
    t.up()
    gotoTransform(-45,20)
    t.down()
    t.seth(180)
    t.fd(10)
    t.up()
    gotoTransform(45,20)
    t.down()
    t.seth(0)
    t.fd(10)
#画尾巴
def initTail():
    t.fillcolor('yellow')
    t.up()
    gotoTransform(65,-140)
    t.down()
    t.begin_fill()
    t.seth(10)
    t.fd(20)
    t.seth(90)
    t.fd(20)
    t.seth(10)
    t.fd(10)
    t.seth(80)
    t.fd(100)
    t.seth(35)
    t.fd(80)
    t.seth(260)
    t.fd(100)
    t.seth(205)
    t.fd(40)
    t.seth(260)
    t.fd(37)
    t.seth(205)
    t.fd(20)
    t.seth(260)
    t.fd(25)
    t.seth(175)
    t.fd(30)
    t.seth(100)
    t.fd(13)
    t.end_fill()
#摇动尾巴
def TailSwing():
    t.fillcolor('yellow')
    t.up()
    gotoTransform(65,-140)
    t.down()
    t.begin_fill()
    t.seth(10)
    t.fd(20)
    t.seth(40)
    t.fd(20)
    t.seth(10)
    t.fd(10)
    t.seth(80)
    t.fd(100)
    t.seth(35)
    t.fd(80)
    t.seth(260)
    t.fd(100)
    t.seth(205)
    t.fd(40)
    t.seth(260)
    t.fd(37)
    t.seth(205)
    t.fd(20)
    t.seth(260)
    t.fd(25)
    t.seth(175)
    t.fd(40)
    t.seth(100)
    t.fd(23)
    t.end_fill() 
#初始化
def init():
    initEars()
    initFoots()
    initTail()
    initBody()
    initFace()
    initHands()
    initEyes()
#闭眼
def upgarde():
    initEars()
    initFoots()
    TailSwing()
    initBody()
    initFace()
    initHands()
    closeEyes()
#睁眼
def upgardeInit():
    initEars()
    initFoots()
    initTail()
    initBody()
    initFace()
    initHands()
    initEyes()
def main():
    t.tracer(False)
    init()
    for i in range(50):
        if i % 2 == 0:
            t.reset()#清空窗口
            t.hideturtle()#隐藏画笔
            upgarde()
            t.update()#更新窗口
            time.sleep(0.3)
        else:
            t.reset()#清空窗口
            t.hideturtle()#隐藏画笔
            upgardeInit()
            t.update()#更新窗口
            time.sleep(0.3)
    t.done()

# t.tracer(False)
# upgardeInit()
# t.done()
# initTail()
# TailSwing()




