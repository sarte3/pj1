import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #특수키 사용
driver=webdriver.Chrome('data\\chromedriver')
url='https://pjt3591oo.github.io/'
driver.get(url)
# driver.execute_script('alert("happy day")')
time.sleep(1)
search=driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
search.click()
box=driver.find_element_by_css_selector('#search-box')
box.send_keys('nosql')
box.send_keys(Keys.ENTER)

btn=driver.find_element_by_css_selector('input[type=submit]')
btn.click()