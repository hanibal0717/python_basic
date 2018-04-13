
import requests
from bs4 import BeautifulSoup
from MyCrowring import getSelectList

lis = getSelectList("http://www.k-startup.go.kr/main.do","#divTab01 li")

#print(lis)
for i, li in enumerate(lis):
    print(i, (li.select("a")[0]).attrs.get("title"))