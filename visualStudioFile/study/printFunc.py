import time
import random
#print ('在'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+
#'，我写了人生中第一行Python代码\n它的内容虽然简单，不过是平凡的一句print(520)\n但我知道：我的编程之路，将从最简单的520开始\n在我点击运行的同时，一切在这一刻开始变得不同\n以下，是这行代码的运算结果：')
#print(520)
# stone = random.randint(0,4)
# print(stone)
# print(type(stone))

# list2 = [5,6,7,8,9]
# #
# print(list2[:]) #5,6,7,8,9
# print(list2[2:]) #7,8,9
# print(list2[:2]) #5,6
# print(list2[1:3]) #6,7
# print(list2[2:4]) #7,8

# for i in range(1,5,1):
#     print(random.randint(1,2))

class 类:
    变量 = 100 #类属性

实例1 = 类() # 实例化
实例2 = 类() # 实例化
print(实例1.变量)
print(实例2.变量)
实例1.变量 = 10
类.变量 = 1

print(实例1.变量)
print(实例2.变量)