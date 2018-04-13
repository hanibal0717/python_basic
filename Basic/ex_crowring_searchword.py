'''
# 웹 크롤링
- 웹 크롤링을 하려면 일단 웹프로그래밍에 대한 이해 필수.
- 웹 크롤링은 CSS나 Javascript의 DOM Selector의 이해가 필요.
- 자바나 자바스크립트로도 크롤링이 가능하다.(jSoup)
- 파이썬에서도 크롤링이 가능하다. (bs4 모듈의 BeatifulSoup)
- CSS나 jQuery의 DOM 셀렉터
    - 클래스 선택기 : 점(.)으로 시작
    - 아이디 선택기 : 샵(.)으로 시작
    - 속성 선택기 : 브라켓 대괄호 ([]) 사용
- 정규표현식을 사용하려면 import re

예)
    - div태그중에서 클래스가 a인 태그만 선택
        <div class="a">...</div>
        div.a
    - div태그중에 아이디가 korea인 태그 선택
        <div id="korea">....</div>
        div#korea
    - 속성선택자는
        <img alt="hello" title="hello" src="...">
        img[alt=hello]
'''

import requests
import time
from bs4 import BeautifulSoup

# requests를 이용해서 response 객체를 얻어 온다.
# response객체에는 화면의 요소를 포함하고 있다.
# response객체와 BeautifulSoup를 이용해서 DOM 객체를 얻는다.
# DOM은 문서객체모델(Document Object Model)이다.
# DOM에서 추출한 값은 리스트(list) 형식으로 사용된다.
# 요청 : request
# 응답 : response

response = requests.get("https://www.naver.com/")
assert response.status_code is 200

# print(response)
# response정보에 담긴 내용을 BeautifulSoup를 이용해서 DOM으로 변환

dom = BeautifulSoup(response.content, "html.parser")

# print(dom)
# print(dom.select(".area_logo")[0])
# print(dom.select("div.area_logo > h1 > a > span"))
# print(dom.select("div.flick-panel ul.api_list"))
# print(dom.select("ul.ah_l span.ah_k"))

cnt = 0
while cnt < 10:
    lis = dom.select("ul.ah_l span.ah_k");

    for no, li in enumerate(lis):
        print(no + 1, li.text)

    time.sleep(10)  # 10초에 한번씩 반복~
    cnt += 1

