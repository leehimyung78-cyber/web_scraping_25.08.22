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

# 3. HTML 파싱작업
bs = BeautifulSoup(html, 'html.parser')

a_tags = bs.select('a')
a_tag = bs.select_one('a')
print(a_tag)

for tags in a_tags:
  print(tags.get('href'))
 # 대가로로 감싸져 있음.리스트로 변환되었음.

"""

    # 4. BeautifulSoup 객체 생성
    soup = BeautifulSoup(html, "html.parser")

    # 5. 원하는 데이터 추출 (예: a 태그 중 class="nav" 찾기)
    links = soup.find_all("a")

    for link in links[:10]:  # 처음 10개만 출력
        print(link.get_text(), "➡", link.get("href"))
else:
    print("웹 요청 실패:", response.status_code)
"""