
from MyCrowring import getSelectList


lis = getSelectList("https://www.naver.com/", "ul.ah_l span.ah_k")

for no, li in enumerate(lis):
    print(no + 1, li.text)
    if no == 9:
        break