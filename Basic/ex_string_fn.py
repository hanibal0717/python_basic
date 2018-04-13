# --*-- coding: utf-8 --*--
#python_day02_ex01_string.py
'''
문자열 관련 함수 정리
'''
'''
aa = "Hello Python World"
# 대문자를 소문자로 변환
print(aa.lower())

# 소문자를 대문자로 변환
print(aa.upper())
'''
'''
while True:
	res = input('종료하시려면 q를 입력 하세요>>> ')
	#if res=='Q' or res=='q':
	#	break
	if res.upper() == 'Q':
		break

	print("res ==> ", res)
'''

#특정 문자열 안에 찾고자하는 문자의 갯수 확인
#문자열.count('찾을문자')
'''
aa = "abcd abcd efg abc"
cnt = aa.count("c")
print("c의 갯수:", cnt)
cnt = aa.count("d")
print("d의 갯수:", cnt)
'''

#문자열의 길이를 반환하는 함수
#len(문자열)
'''
aa = "Hello python world!"
length = len(aa)
#print("length =>:", length)
#print(aa,"문자열의 길이는",length )
print("{0}문자열의 길이는{1}개이다.".format(aa, length) )
'''

# 문자의 위치 찾기(find()함수 or index()함수)
## 문자열.find(찾을문자)
## find: 찾을 문자가 없다면 -1을 리턴한다.
'''
aa = "Hello python world!"
idx = aa.find('z')
print('idx=>', idx)
'''

## 문자열.index(찾을 문자열)
# index: 해당 문자가 없으면 error이다.
'''
aa = "Hello python world!"
idx = aa.index('o')
print('idx=>', idx)
'''


# 공백제거함수 : strip, lstrip, rstrip 함수
# 파이썬에서는 trim이 아니고 strip이다.
'''
aa = "   love   "
print(aa + "you")
print(aa.strip() + " you")
print(aa.lstrip() + " you")
print(aa.rstrip() + " you")
'''





# 문자열 대체 함수 : replace
# 문자열.replace(바뀔대상, 새문자열)
# 튜플과 문자열은 직접 수정이 안된다.
# 문자열 교체 결과를 새로운 변수에 대입한다.
# str[find(''morning'):] + 'aa' + str[:4]
# 이런형식이어야 한다.
'''
str = "good morning susan"
str = str.replace("morning","night")
print(str)
'''



# 문자열을 나누는 함수 - split함수
# 문자열을 단어별로 나누어서 결과를 list로 반환한다.
# 디폴트 구분자는 공백이다.
'''
str = "good morning susan"
sList = str.split()
print(sList)
'''

# 특정문자를 구분자로 문자열 분리하기
str = "홍길동|서울시 은평구 응암동|010-1234-5678|프로그래머"
infoList = str.split('|')
print(infoList)
print(type(infoList) )





