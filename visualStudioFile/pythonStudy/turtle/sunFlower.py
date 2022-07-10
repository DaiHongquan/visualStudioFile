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



## 绘制五角星
# turtle.screensize(canvwidth=None,canvheight=None,bg='black')
# turtle.setup(width=0.5,height=0.5,startx=None,starty=None)
# turtle.speed(2)
# turtle.pencolor('red')
# turtle.fillcolor('yellow')
# turtle.begin_fill()
# turtle.up()
# count = 1 #计时器用于记录次数
# while count <=5:
#     turtle.down()
#     turtle.forward(250)
#     turtle.right(144)
#     count += 1
    
# turtle.end_fill()
# turtle.done()

##绘制太阳花
# t.screensize(400,300)
# t.setup(840,500)
# t.pensize(2)
# t.color('red','yellow')
# t.speed(10)
# t.up()
# t.goto(-150,0)
# t.down()
# t.begin_fill()
# while True:
#     t.forward(300)
#     t.left(170)
#     if t.distance(-150,0) < 1:
#         break;
# t.end_fill()
# t.done()


##绘制四叶草
#turtle.circle(raidus,extent=None,steps=None)#r半径，e弧度，s做半径为日的圆的内切正多边形，s为多边形边数
# t.screensize(400,300)
# t.setup(840,500)
# t.pensize(5)
# t.color('mediumseagreen','forestgreen')
# t.speed(10)
# def draw_clover(radius,rotate):
#     t.begin_fill()
#     for i in range(4):
#         direction = i * 90
#         t.seth(60 + direction + rotate)
#         t.fd(4 * radius)
#         for j in range(2):
#             t.seth(90 + direction + rotate)
#             t.circle(radius,180)
#             t.seth(-60 + direction + rotate)
#             t.fd(4 * j * radius)
#             t.seth(60 + direction + rotate)
#             t.fd(2 * j * radius)
#         for j in range(2):
#             t.pencolor('whitesmoke')
#             t.pensize(8)
#             t.seth(90 + direction + rotate)
#             t.circle(radius / 2,180)
#             t.color('mediumseagreen','forestgreen')
#             t.pensize(5)
#         t.seth(-60 + direction + rotate)
#         t.fd(2 * radius)
#     t.end_fill()
#     t.seth(-110)
#     t.fd(6 * radius)

# draw_clover(40,30)
# t.done()

##绘制狮子头
t.screensize(400,300)
t.setup(840,500)
t.speed(10)
#画头发
def hair():
    t.up()
    t.goto(-70,125)
    t.down()
    t.fillcolor('saddlebrown')
    t.begin_fill()
    for j in range(12):
        t.seth(60 - (j * 30))
        t.circle(-50,90)
    t.end_fill()
#画耳朵 dir用来设置方向，左右耳对称
def ears(dir):
    t.penup()
    t.goto((0 - dir) * 25,75)
    t.seth(90)
    t.down()
    t.fillcolor('peru')
    t.begin_fill()
    t.circle(dir * 28)
    t.end_fill()
    t.up()
    t.goto((0 - dir) * 30,68)
    t.seth(90)
    t.down()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir * 18)
    t.end_fill()

#画脸
def face():
    t.up()
    t.goto(0,80)
    t.down()
    t.fillcolor('peru')
    t.begin_fill()
    t.seth(180)
    t.circle(80)
    t.end_fill()
    #下巴
    t.circle(80,125)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(80,110)
    t.seth(145)
    t.circle(110,72)
    t.end_fill()

#画眼睛 dir用来设置方向，左右眼对称
def eye(dir):
    t.up()
    t.goto((0 - dir) * 30,20)
    t.seth(0)
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
#画嘴巴
def mouth():
    t.up()
    t.goto(0,0)
    t.seth(-90)
    t.down()
    t.fd(50)
    t.seth(0)
    t.circle(80,25)
    t.up()
    t.goto(0,-50)
    t.seth(180)
    t.down()
    t.circle(-80,25)

#画鼻子
def nose():
    t.up()
    t.goto(15,0)
    t.seth(90)
    t.down()
    t.fillcolor('saddlebrown')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()

t.done()

    

