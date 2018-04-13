# --*-- coding: utf-8 --*--
'''
리스트 활용하기
'''
peoples = [
	['길동', 50,50,50,0,0.0,'A'],
	['길순', 90,90,90,0,0.0,'A'],
	['길자', 70,70,70,0,0.0,'A'],
	['순자', 80,80,80,0,0.0,'A'],
	['말자', 60,60,60,0,0.0,'A']
]

for i, li in enumerate( peoples):
	for j in range(1, 4):
		li[4] += li[j]
	li[5] = li[4] / 3.0
	if li[5] >= 90:
		li[6] = 'A'
	elif li[5] >= 80:
		li[6] = 'B'
	elif li[5] >= 80:
		li[6] = 'C'
	elif li[5] >= 80:
		li[6] = 'D'
	else:
		li[6] = 'F'

for people in peoples:
	print(people)