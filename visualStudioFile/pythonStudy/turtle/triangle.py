#导入海龟绘图库
from itertools import count
from turtle import *
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

##绘制谢尔宾斯基三角形

screensize(400,300)
setup(840,500)
speed(10)

#传入列表中三个点的坐标绘制三角形
def draw_triangle(size):
    up()
    goto(size[0])
    down()
    goto(size[1])
    goto(size[2])
    goto(size[0])

#计算返回任意2个点的中间坐标
def get_mid(a,b): 
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return [x,y]  
#递归调用times次，调用绘制函数draw_triangle(size)
def draw_s(size,times):
    draw_triangle(size)
    if times > 1:
        #绘制左边小三角形
        size2 = [size[0],get_mid(size[0],size[1]),get_mid(size[0],size[2])]
        draw_s(size2,times - 1)
        #绘制上边的小三角形
        size3 = [get_mid(size[0],size[2]),get_mid(size[1],size[2]),size[2]]
        draw_s(size3,times - 1)
        #绘制右边的小三角形
        size4 = [get_mid(size[0],size[1]),size[1],get_mid(size[1],size[2])]
        draw_s(size4,times - 1)
left(90)
points = [[-200,-150],[200,-150],[0,150]]
count = 5
draw_s(points,count)
done()