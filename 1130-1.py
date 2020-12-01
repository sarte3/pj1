import time
from  selenium import webdriver
driver=webdriver.Chrome('data\\chromedriver')
url='https://www.10000recipe.com/recipe/list.html'
driver.get(url)
a2 = driver.find_element_by_css_selector('#id_search_category div.cate_list > a:nth-child(2)')
# print(a2.text)
# print(a2.get_attribute('href'))
driver.execute_script('''goSearchRecipe('cat4','63')''') #파이썬에서 js 호출방법

