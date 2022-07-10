#导入海龟绘图库
from cgi import print_environ
from turtle import *
from datetime import *

from matplotlib.axis import Tick
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
# turtle.register_shape(x,y)#注册合法的外形

##画时钟

screensize(400,300)
setup(840,500)

#抬起画笔，向前运动一段距离放下
def skip(step):
    up()
    fd(step)
    down()

#定义指针几何形状
def mkHand(name,length):
    reset()
    skip(-length * 0.1)
    begin_poly()
    fd(length * 1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name,handForm)

#初始化表针和文本对象
def init():
    global secHand,minHand,hurHand,printer
    mode('logo')
    mkHand('secHand',145)
    mkHand('minHand',120)
    mkHand('hurHand',90)
    secHand = Turtle()
    secHand.shape('secHand')
    minHand = Turtle()
    minHand.shape('minHand')
    hurHand = Turtle()
    hurHand.shape('hurHand')
    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)#设置表征形状大小为3像素
        hand.speed(0)
    printer = Turtle()
    printer.hideturtle()
    printer.up()
#画表盘
def setupClock(radius):
    reset()
    pensize(6)
    color('#0A0A0A','green')
    #定义一个i值，遍历i值，根据条件画出时钟的各个点与i到12的数字
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            fd(20)
            
            
            if i == 0:
                write(int(12),align='center',font=('Courier',14,'bold'))
                skip(-radius - 20)
            elif i == 30:
                skip(25)
                write(int(i / 5),align='center',font=('Courier',14,'bold'))
                skip(-25)
                skip(-radius - 20)
            elif (i == 25 or i == 35):
                skip(20)
                write(int(i / 5),align='center',font=('Courier',14,'bold'))
                skip(-20)
                skip(-radius - 20)
            else:
                
                write(int(i / 5),align='center',font=('Courier',14,'bold'))
                skip(-radius - 20)
        else:
            dot(5)#绘制一个指针直径为5的圆点
            skip(-radius)
        right(6)

#绘制表针的动态显示
def tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.seth(6 * second)
    minHand.seth(6 * minute)
    hurHand.seth(30 * hour)
    tracer(False)
    printer.home()
    tracer(True)
    ontimer(tick,100)

def main():
    tracer(False)
    init()
    setupClock(180)
    tick()
    mainloop()

if __name__ == '__main__':
    main()


