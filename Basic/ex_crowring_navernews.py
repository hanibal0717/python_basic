# -*- coding:utf-8 -*-

from MyCrowring import getSelectList

lis = getSelectList("http://news.naver.com/", "div.main_component");

# print(lis)
for i, li in enumerate(lis):
    if li.select("h4"):
        title = li.select("h4")
        print(title[0].text)

    lists = li.select("li a")
    for item in lists:
        print(item.text)

    print("-" * 50)

# 정규표현식
for i in range(20):
    if i >= 10:
        val = i
    else:
        val = "0" + str(i)
    s = "book_tile_{}".format(val)
    print(s)

