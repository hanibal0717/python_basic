# --*-- coding: utf-8 --*--
"""
파이썬에서 주로 사용되는 자료구조
# 리스트와 튜플은 거의 같은 구조이나 튜플은 수정이 안된다.
# 대신 튜플은 속도가 빠른 장점이 있다.
- 리스트 [1,2,3,4]
- 튜플 (1,2,3,4)
- 딕셔너리 {key:value, key:value ...}
- Set 구조는 인덱스나 키가 없고 값만 저장한다.
"""
aa = [10,20,30]
print(aa)
for num in aa:
	print("num =>", num)
print("-"*50)
for idx, num in enumerate(aa):
	print(idx, "num =>", num)

#문자열을 리스트로 바로 변환
strLis = list("abcdefgh")
print("strLis >>> ", strLis)



bb = [1,2,3,4,5,6,7,8,9]
print( bb[2] + bb[5])
print(bb)
#리스트는 값을 직접 변경 할수 있다.
bb[4] = 500
print(bb)


# 리스트구조에 넣을수 있는 타입은 제한이 없다.
cc = [10, 'A', [1,'KOREA',3]]
print(cc)

print(cc[2][1])

dd = [10,20,30,['a','b',["AA","BB","CC"],'c']]
print(dd[3][2][1])