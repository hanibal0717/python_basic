import requests
import time
from bs4 import BeautifulSoup


def getSelectList(juso, selector):
    response = requests.get(juso)
    assert response.status_code is 200

    dom = BeautifulSoup(response.content, "html.parser")
    lis = dom.select(selector);

    return lis;


cnt = 0
while cnt < 10:
    lis = getSelectList("https://www.naver.com/", "ul.ah_l span.ah_k")

    for no, li in enumerate(lis):
        print(no + 1, li.text)

    time.sleep(10)  # 10초에 한번씩 반복~
    cnt += 1

