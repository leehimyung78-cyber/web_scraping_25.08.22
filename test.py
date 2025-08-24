import requests
from bs4 import BeautifulSoup

# 1. URL 지정
url = "https://land.naver.com/news/headline.naver"

# 2. 웹페이지 요청
response = requests.get(url)

html = """
<nav class="menu-box-1" id="menu-box-1">
  <ul>
    <li>
      <a href="https://land.naver.com/news/headline.naver">네이버부동산으로 이동</a>
    </li>
    <li>
      <a href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""
"""
# 3. HTML 파싱작업
bs = BeautifulSoup(html, 'html.parser')

# 첫번째로 일치하는 단일 요소 접근
a_tag = bs.select_one('a')

# 모든 일치하는 요소로 접근할 때 사용, 리스트로 반환
a_tags = bs.select('a')
print(a_tag)

# get_text() : 해당 엘리먼트가 품고있는 텍스트 추출
for tags in a_tags:
  print(tags.get_text()) 
  
# get('href') : 해당 엘리먼트가 가지고 있는 속성값을 추출출
for tags in a_tags:
  print(tags.get('href')) 
"""