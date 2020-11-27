# from selenium import webdriver
# # 웹드라이버 : 크롤러와 브라우저를 연결시켜주는 프로그램
# # 크롬드라이버 다운로드
# # driver.find_element_by_class_name()
# # driver.find_elements_by_class_name()
# # driver.find_element_by_css_selector()
# # driver.find_elements_by_css_selector()
#
# # 마우스제어 click()
# # 키보드제어 send_keys()
# # 자바스크립트실행 execute_script()
#
#
# url ='https://pjt3591oo.github.io/'
# driver=webdriver.Chrome('data\\chromedriver')
# driver.get(url)
# # a = driver.find_element_by_css_selector('body > main > div > div > div:nth-child(9) > h3 > a')
# # print(a.tag_name)
# # print(a.text)
# # a.click()
#
# import time
#
# url ='https://pjt3591oo.github.io/'
# driver=webdriver.Chrome('data\\chromedriver')
# driver.get(url)
# # print("현재 페이지 소스", driver.page_source)
# # print("현재 URL", driver.current_url)
# # print("title 태그", driver.title)
#
# time.sleep(1)
# search = driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
# search.click()
# box = driver.find_element_by_css_selector('#search-box')
# box.send_keys('python')
# btn = driver.find_element_by_css_selector('input[type=submit]')
# btn.click()
# # 파란제목 출력
#
# h3s = driver.find_elements_by_css_selector('#search-results > li > a > h3')
# for h3 in h3s:
#     print(h3.text)
#
# from selenium import webdriver
# import time
#
# def getPW():
#     with open('d:\\pw.txt') as f:
#         pw = f.readline()
#         return pw.strip()
#
# driver = webdriver.Chrome('data\\chromedriver')
# url = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
# driver.get(url)
# time.sleep(1)
# idbox = driver.find_element_by_css_selector('#id')
# idbox.send_keys('insomnia4u')
# time.sleep(1)
# pwbox = driver.find_element_by_css_selector('#inputPwd')
# pwbox.send_keys(getPW())
# btn = driver.find_element_by_css_selector('#loginBtn')
# time.sleep(1)
# btn.click()
# time.sleep(1)
# driver.get('https://mail.daum.net/')
# time.sleep(1)
# # print(driver.page_source)
# # 보낸 사람, 메일 제목 출력
# senders = driver.find_elements_by_css_selector('div.info_from > a')
# titles = driver.find_elements_by_css_selector('div.info_subject > a.link_subject > strong')
#
# for s, t in zip(senders, titles):
#     print(s.text, t.text)

# from selenium import webdriver
# import time


# def getPW():
#     with open('d:\\pw.txt') as f:
#         pw = f.readline()
#         return pw.strip()
#
#
# driver = webdriver.PhantomJS('data\\phantomjs')
#
# url = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
# driver.get(url)
# time.sleep(1)
# idbox = driver.find_element_by_css_selector('#id')
# idbox.send_keys('insomnia4u')
# time.sleep(1)
# pwbox = driver.find_element_by_css_selector('#inputPwd')
# pwbox.send_keys(getPW())
# btn = driver.find_element_by_css_selector('#loginBtn')
# time.sleep(1)
# btn.click()
# time.sleep(1)
# driver.get('https://mail.daum.net/')
# time.sleep(1)
# # print(driver.page_source)
# # 보낸 사람, 메일 제목 출력
# senders = driver.find_elements_by_css_selector('div.info_from > a')
# titles = driver.find_elements_by_css_selector('div.info_subject > a.link_subject > strong')
#
# for s, t in zip(senders, titles):
#     print(s.text, t.text)

from selenium import webdriver
import time
from bs4 import BeautifulSoup


def getPW():
    with open('d:\\pw.txt') as f:
        pw = f.readline()
        return pw.strip()

driver = webdriver.Chrome('data\\chromedriver')
url = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
driver.get(url)
time.sleep(1)
idbox = driver.find_element_by_css_selector('#id')
idbox.send_keys('insomnia4u')
time.sleep(1)
pwbox = driver.find_element_by_css_selector('#inputPwd')
pwbox.send_keys(getPW())
btn = driver.find_element_by_css_selector('#loginBtn')
time.sleep(1)
btn.click()
time.sleep(1)
driver.get('https://mail.daum.net/')
time.sleep(1)
# print(driver.page_source)
# 보낸 사람, 메일 제목 출력
dom = BeautifulSoup(driver.page_source, 'lxml')

senders = dom.select('div.info_from > a')
titles = dom.select('div.info_subject > a.link_subject > strong')

for s, t in zip(senders, titles):
    print(s.text.strip(), t.text.strip())
