


import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20211026094946429'

# 1.requests 라이브러리 사용해서 해당 URL의 소스코드 가져오기
result = requests.get(url)

# 2.BeautifulSoup 라이브러리 사용해서 원하는 정보만 추출
doc = BeautifulSoup(result.text, 'html.parser')

#select 사용해서 데이터를 수집 => list type []
# h3 tag 중에서 class 가 tit_view인 tag를 가져오세요
title = doc.select('h3.tit_view')[0].get_text() # . =>class

