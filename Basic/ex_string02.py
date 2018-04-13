# --*-- coding: utf-8 --*--

"""
문자열 교체
"""
aa = "ABCDEFG"
print(aa)

#문자열은 직접 수정이 불가능하다.
#aa[2] = 'Z'
#print(aa)

#print(aa[:2])
#print(aa[3:])

#교체를 하려면 잘라서 재 조합한다.
aa = aa[:2] + 'Z' + aa[3:] # 문자열의 2번지가 교체
print(aa)
print(aa)