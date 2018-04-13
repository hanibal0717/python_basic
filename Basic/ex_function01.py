# --*-- coding: utf-8 --*--
# python_day02_ex03_function.py
# 사용자 정의 함수
# 파이썬에서 함수를 선언할때는 def예약어를 사용
# 함수명 뒤에 괄호는 매개변수를 넣어주는 기능
# 매개변수=인수=인자=parameter=argument 모두 같은 의미
## 함수를 선언하는 부분
'''
--- 탭(Tab key)을 이용해서 블럭(몸체)을 구분한다.
def 함수명():
	실행문1
	실행문2
	실행문n

'''
'''
def myFunc():
	print("사용자 정의함수 myFunc");

## 함수를 호출하는 부분
## 함수를 호출하지 않으면 함수는 실행하지 않는다.
# 내가 너의 이름을 불러주었을때 너는 꽃이 되었다.
myFunc()
'''
'''
def maximum(x, y):
	if x>y:
		print(str(x)+"가 더 크다")
	elif y>x:
		print(str(y)+"가 더 크다")
	else:
		print(str(x)+"와 "+str(y)+"가 같다")

maximum(20,30)
'''

# 인자와 반환값을 모두 사용하는 함수
'''
def maximum(x, y) :
	if x > y:
		return x
	else:
		return y

print(maximum(30, maximum(10,20)) )
'''

# 매개변수가 없고 리턴문만 있는 함수
'''
str1 = "Hello python world!"
def getStr() :
	return str1

print(getStr())
'''


# 정수를 입력받아서 돌려주는 함수
'''
def choiceMenu() :
	print("1.input 2.output 3.search 4.end")
	no = input("Choice>>> ")
	return int(no)


while True:
	i = choiceMenu()
	if i==4:
		break
'''

# 성명과 주소를 입력 받아서 반환하는
# getInfo 함수를 선언하세요.
'''
def getInfo():
	name = input("성명입력>>> ")
	addr = input("주소입력>>> ")
	p = []
	p.append(name)
	p.append(addr)
	return p
'''
'''
def getInfo():
	name = input("성명입력>>> ")
	addr = input("주소입력>>> ")
	return name, addr 
	#파이썬은 2개 이상의 반환값을 전달가능.
	#튜플로 전달 된다.

print(getInfo())
'''
'''
def fn01():
	print("fn01() 함수")

def fn02(fn):
	fn()

#함수의 인자값으로 다른 함수를 사용.
#일종의 전략패턴 or 템플릿메소드 패턴
fn02(fn01)
'''

def funcA():
	print("funcA 함수")

def funcB():
	print("funcB 함수")

def funcC():
	print("funcC 함수")

factory = [funcA, funcB, funcC]

while True:
	no = int(input("1.A 2.B 3.C 4.End >>>") )
	if no ==4: break
	factory[no-1]()