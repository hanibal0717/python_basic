import requests
from bs4 import BeautifulSoup

def getSelectList(juso, selector):
    response = requests.get(juso)
    assert response.status_code is 200

    dom = BeautifulSoup(response.content, "html.parser")
    lis = dom.select(selector)

    return lis