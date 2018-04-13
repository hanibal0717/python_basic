# --*-- coding: utf-8 --*--
"""
리스트의 연산
"""
'''
aa = [1,2,3,4,5,6,7,8,9]
aa[4] = 500
print(aa)

aa[4:] = [1000,2000,3000,4000]
print(aa)

aa[4] = ["aa","bb","cc"]
print(aa)
'''

# 난수발생기 : random모듈을 import해야 한다.
import random
import turtle

#num = random.randint(10, 50) # 10부터 50미만의 랜덤 갑쇼
#print(num)

t = turtle.Turtle()
t.speed(0)
t.pencolor('red')
t.width(3)
for i in range(1000):
	length = random.randint(10,100)
	angle = random.randint(0,360)
	t.forward(length)
	t.left(angle)

