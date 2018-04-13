# --*-- coding: utf-8 --*--

# set 자료구조 생성
s = set("Abcd12defsabc")
print(s)

s.remove('A')
#remove로 없는 데이터를 지우면 Error 발생
#s.remove('z')

#discard를 이용해서 지우면 에러발생 안함.
s.discard('a')
s.discard('z')

#요소의 갯수 알아내기
_size = len(s)
print("요소의 갯수:", _size)

# set데이터를 list 자료구조료 변경
lis = list(s)
lis.sort()
lis.reverse()
print(lis)