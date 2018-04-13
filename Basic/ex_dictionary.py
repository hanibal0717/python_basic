# --*-- coding: utf-8 --*--
# 딕셔너리
# 딕셔너리의 아이템은 Key 와 Value 의 쌍으로 이루어진다.
#  dic = {key:value, key:value ...}

'''
#딕셔너리 사용
sports = {"축구":"박지성","피겨":"김연아","체조":"손연재"}
print(sports["축구"])
print(sports["피겨"])
print(sports["체조"])
'''
'''
#딕셔너리의 값 변경
aa = {1:"안녕", 2:"하이"}
print(aa)

aa[3] = "방가"
print(aa)

aa["인사"] = "굿모닝"
print(aa)

aa[3]=[1,2,"Korea","Japan"]
print(aa)

del aa[1]
print(aa)

aa[1] = "We"
print(aa)
'''

'''
#딕셔너리를 만들어주는 함수
a = {(1,2,3):[10,20,30]}
#print(a)
#print(a.keys())
#print(a[(1,2,3)])
print(a.keys())
for i in a.keys():
	if 1 in i:
		print("1 이 포함 되었다")
	if 2 in i:
		print("2 가 포함 되었다")
	if 3 in i:
		print("3 이 포함 되었다")
'''

'''
#딕셔너리의 튜플키 활용
a = {(1,2,3):[10,20,30]}
val = int(input("정수 입력: "))
key1 = (1,2,3)
if val in key1:
	print("포함된 키값이 있다")
	print(a[key1])
'''
'''
#딕셔너리를 만들어주는 함수
#dic = dict() #항목(item)이 없는 딕셔너리 생성.
#dic = {}
#ss = "{'학교':'서울대학교','학번':'1818181818'}"
#dic = dict(ss)
#dic = dict({'학교':'서울대학교','학번':'1818181818'})
dic = {'학교':'서울대학교','학번':'1818181818'}
print(dic)

dic['first'] = "첫째"
print(dic)
'''
'''
lists = list("Hello world");
print(lists)
'''


#key값을 dict_keys타입으로 반환하는 함수 >>> keys()
sports = {"축구":"박지성","피겨":"김연아","체조":"손연재"}
print(sports)

sports_items = sports.items()
print(sports_items)
sports_keys = sports.keys()
print(sports_keys)
sports_values = sports.values()
print(sports_values)
'''
#dict_keys 타입을 리스트 타입으로 변환
dictkeyList = list(sports.keys())
print(type(dictkeyList) )
print(dictkeyList)
'''


