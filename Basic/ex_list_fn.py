# --*-- coding: utf-8 --*--
# list관련 함수 정리

# 리스트에 값을 추가하는 함수 - append()
'''
li = [10, 100, 1000]
print(len(li), li)
li.append(1010)
#[idx]로 값을 변경할때는 범위내에서만 변경 가능
#li[3] = 1010
print(len(li), li)
# 리스트는 요소의 타입에 구분이 없다.
li.append('Korea')
print(li)

# 다른 리스트도 리스테에 append 가능.
li.append(['a','b'])
print(li)
'''
'''
li = [1,5,2,7,8,4,9,3]
print(li)

# 리스트 정렬하기 : sort()
li.sort()
# 리스트 요소의 순서 바꾸기 : reverse()
li.reverse()
print(li)

# 리스트의 문자요소 정렬
## 리스트로 변환하는 함수 list()
li = list('hello world')
print(li)
li.sort()
print(li)
'''
'''
# 리스트에 요소를 추가 : insert() 함수
li = [1,2,3,4,5]
# 해당 위치를 지정해서 새로운 값 삽입
li.insert(2,6)
print(li)
'''

# 요소의 위치 반환
'''
li = [1,2,3,4,5]
#idx = li.find(3)
idx = li.index(3)
print(idx)
'''


# 리스트에서 요소를 제거한다 : remove()함수
'''
list2 = [22,33,4,5,6,66,99]
val0 = list2.remove(66) # remove는 끄집어 내지 않는다.
val = list2.pop()
val2 = list2.pop(1) # 끄집어 내고 제거한다.
print(val, "-", list2, "-", val0, "-", val2)


# 요소의 갯수를 파악하는 함수 - count() 함수
list2 = [22,33,4,5,6,66,99,4,33]
cnt = list2.count(4)
print("cnt:", cnt)
'''

# 리스트를 확장하는 함수 - extend() 함수
'''
list3 = [1,2,3]
list3[len(list3):] = [4,5,6,7]
print(list3)
'''
'''
list3 = [1,2,3]
list3.extend([4,5,6,7])
print(list3)
'''
list3 = [1,2,3]
list3 += [4,5,6,7]
print(list3)


# 파이썬식 swap
a = 10
b = 30
print("a:{}, b:{}".format(a, b) )
(a,b) = (b,a)
print("a:{}, b:{}".format(a, b) )

# 다른 언어에서 swap
tmp = a
a = b;
b = tmp
print("a:{}, b:{}".format(a, b) )


