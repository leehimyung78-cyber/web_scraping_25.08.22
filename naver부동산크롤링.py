
import requests
from bs4 import BeautifulSoup

# 뉴스 제목을 나타내는 a태그만의 별명을 이용해서 선택해야 한다.(원하는 태그를 선택하는 방법)
# 별명은 'calss'와 'id'가 있으므로 이것을 찾아 테스트를 할 수 있다.
# class = . , id = #

response = requests.get('https://land.naver.com/news/headline.naver?page=1')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# select는 해당되는 내용 전체를
# select_one은 해당되는 내용 하나만
links = soup.find_all('div', id_='.content') # 결과는 리스트 형태
title.get_text()


"""
from urllib.parse import urljoin #상대값과 절대값이 섞일 수 있으므로 일관처리
import requests
from bs4 import BeautifulSoup

naver_url = "https://land.naver.com/news/headline.naver?page={}"

for page in range(1, 6):   #1~5페이지까지
    url = naver_url.format(page)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"\n=== {page} 페이지 뉴스 ===")
    
    # 기사 제목과 링크 추출
    news_links = soup.select("ul.headline_list li a") # 기사 a로 된 태그 선택
    for a in news_links:
        title = a.get_text(strip=True)
        link = a["href"]
        print("-", title, ":", link)
  """