# web scraping 을 위해 설치해야할 것들
# pip install requests
# pip install bs4

import requests #html문서를 호출
from bs4 import BeautifulSoup #html문서안에서 의미있는 애들을 추출

res = requests.get('https://www.naver.com/')
print("#"*30,res) #HTTP status code 를 반환합니다.  200번은 성공이라는 뜻입니다.
# print(res.text) #반환값은 HTML문서로 반환됩니다.

myhtml = res.content 

data = BeautifulSoup(myhtml, 'html.parser') #bs4를 이용해서 추출(parsing)할 대상과 추출할 방법에 대해서 설정해줍니다. 
# print(data)


# find() : ()에 들어갈수 있는 요소들 tag name, class, id
# get_tag = data.find('title')  --- tag name
# get_tags_all = data.find_all('div')  --- tag name + multiple

# get_id = data.find("div", id="u_skip") --- id 
# get_class = data.find("i", class_="_1KncATpM") --- class

# print(get_tag)
# print("###########")
# print(get_tags_all)
# print("###########")
# print(get_id.text)   --- 가져온 element의 text만 보자.
# print("###########")
# print(get_class.text)


# data.select() : tag, classname, id / list의 형태로 반환합니다. (~ find_all)

# .className \ #id \ div \ myclass > myclass2 

# select_class = data.select('.className') # class값으로 가져오는 예입니다.  / #id / tag 사용가능
# print(select_class)

# for i in select_class: -- select로 가져오게되면 list의형태로 반환되므로 for문으로 해체할 수 있습니다
# select_class[0] -- list의 형태이므로 indexing을 해줄수도 있습니다.

# select_child = data.select('.nav > i') # CSS의 자식선텍자와 같은 계층구조를 사용할 수 있다.
# print(select_child,"#####")


# seleninum을 ㅆ
# pip install seleninum

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

chromedriver = 'C:/Users/jangc/Desktop/멋직3기 실습자료/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

driver.get('https://naver.com')

search_box = driver.find_element_by_name('query') #검색창을 driver에서 뽑아서 가져옵니다.
search_box.send_keys('날씨') #검색창에다가 data를 보냅니다.
# search_box.send_keys(Keys.RETURN) # 엔터 
driver.find_element_by_id('search_btn').click() # 검색 버튼 클릭



# 아래는 이번주 날씨를 가져오는 간단한 예입니다.
week_whether = driver.find_elements_by_css_selector('._pageList .date_info')
print("< 이번주 날씨 > ")
for i in week_whether:
    if i.find_elements_by_css_selector('.day_info')[0].text:   # 만약 날씨 text가 존재할때만 print해줍니다.
        print( f"{i.find_elements_by_css_selector('.day_info')[0].text}의 기온은 {i.find_elements_by_css_selector('dl dd')[0].text}입니다." )

# time.sleep(10) #10초간 프로그램을 중지시킵니다
# driver.quit() #driver를 종료 시키자.


# 추가로 알아보면 좋을 키워드
# Seleninum sleep 
# https://selenium-python.readthedocs.io/api.html?highlight=click()#selenium.webdriver.remote.webelement.WebElement.click
# Phantom js(브라우저가 실행되지않고 돌아간다. 터미널 상에서 스크래핑을 할때 좋다.)
