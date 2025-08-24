import requests
from bs4 import BeautifulSoup

# 네이버부동산뉴스 1개 크롤링
url = 'https://n.news.naver.com/article/648/0000039129'

# rest : response의 약자
# 지정 웹 사이트의 get요청을 보내서
# request를 이용해서 웹페이지의 html 문서 내용 가져오기
resp = requests.get(url)

# 웹 페이지의 HTML 내용을 Beautifulsoup 객채로 변환
soup = BeautifulSoup(resp.text, 'html.parser')

# 헤드라인을 soup 파인드_올로 접근 h2를 접근할건데 클래스이름이 'media_end_head_headline'  
head_line = soup.find_all('h2', class_='media_end_head_headline') 
print(head_line) # 프린트로 헤드라인을 출력

head_line_list = [] # 빈 리스트를 만들 수 있다.

for title in head_line: # 반복문을 이용해서 타이틀을 텍스트만 가지고 온다.
  head_line_list.append(title.get_text()) # 담을수도 있다.

print(head_line_list)
  