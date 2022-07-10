#导入海龟绘图库
from calendar import c
from operator import le
from turtle import *
from random import *
from math import *

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
# turtle.tracer(n=None,delay=None)#窗口每隔delay秒刷新n次 
# turtle.ontimer(x,y)#在y毫秒后继续调用x方法


##画樱花树
class Tree:
    hideturtle()
    def __init__(self):
        setup(1000,700)
        #bgcolor(1,1,1)
        speed(10)
        tracer(0,0)
        up()
        backward(100)
        left(90)
        backward(300)

    def tree(self,n,l):
        
        down()
        t =cos(radians(heading() + 45)) / 8 + 0.25
        pencolor(t,t,t)
        pensize(n / 1.2)
        #加长树干
        if(l == 100):
            fd(-100)
            backward(-100)
        forward(l)#画树枝
        if n > 0:
            b = random() * 15 + 10#右分支偏转角度
            c = random() * 15 + 10#左分支偏转角度
            d = l * (random() * 0.25 + 0.7)#下一个分支的长度
            right(b)
            self.tree(n - 1,d)
            left(b + c)
            self.tree(n - 1,d)
            right(c)
        else:
            #画叶子
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            color((n,n * 0.8, n * 0.8),(n,n * 0.8, n * 0.8))
            begin_fill()
            circle(3)
            left(90)
            end_fill()
            #添加0.3倍的飘落叶子
            if random() > 0.7:
                up()
                t = heading()
                an = -40 + random() * 40
                seth(an)
                dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
                fd(dis)
                seth(t)
                #画叶子
                down()
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5 
                color((n * 0.5 + 0.5,0.4 + n * 0.4,0.4 + n * 0.4),(n,n * 0.8,n * 0.8))
                begin_fill()
                circle(2)
                left(90)
                end_fill()
                up()
                t = heading()
                seth(an)
                backward(dis)
                seth(t)
        up()
        backward(l)
def main():
    bgcolor(0.5,0.5,0.5)
    tree = Tree()
    tree.tree(12,100)
    tracer(True)
    done()

if __name__ == '__main__':
    main()
