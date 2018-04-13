# --*-- coding: utf-8 --*--
# 가변적 매개변수 - *을 이용한 매개변수 선언
'''
def total( *a ):
	tot = 0
	for i in a:
		tot += i
	return tot

#tup = [1,2,3,4,5,6,7,8,9,10]
#매개변수가 여러개인것이지 리스트나 튜플이 아님
res = total(1,2,3,4,5,6,7,8,9,10)
print("res=>", res)
'''

# 인수에 초기값을 설정하는 방법
# 앞에 초기화 하는 인수가 있다면 뒤에 보통 인수가 올수없다.

def show(name, age=0, gender='F'):
	print("name=>", name)
	print("age=>", age)
	print("gender=>", gender)

show('HONG', 23, 'M')
print("-"*50)
show('KIM', 23)