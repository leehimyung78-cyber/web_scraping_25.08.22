import requests
from bs4 import BeautifulSoup

# 네이버 부동산 뉴스 url
# resp = reponser의 약자
# 지정 웹 사이트의 get요청을 보내서
# requests를 이용해서 웹페이지의 HTML의 문서 내용 가져오기
# 웹 페이지의 HTML 내용을 Beautifulsoup 객체로 변환 
url = 'https://n.news.naver.com/article/648/0000039129'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# 기사 블록 단위로 찾기 (예: div.news_area 같은 구조일 경우)
# 제목
main_titles = soup.find_all('h2', class_="media_end_head_headline") 
for headline in main_titles:
    title_1 = headline.get_text(strip=True)
    
# 날짜    
date = soup.find_all("span", class_="media_end_head_info_datestamp_time _ARTICLE_DATE_TIME")
for time in date:  
    date = time.get_text(strip=True)
# 부제목
article = soup.find('article', id="dic_area")
sub_titles = [st.get_text(strip=True) for st in article.find_all("strong")] # 부제목 태그만 추출

clean_sub_titles = [st for st in sub_titles if "선데이부동산" not in st]

# 출력      
print("제목:", title_1)
print("날짜:", date)
print("부제목:")
for st in clean_sub_titles:
    print("-",st)

