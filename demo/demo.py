from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATh = r"C:\Users\12158\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATh)

driver.get("https://search.bilibili.com/?from_source=webtop_search")
# print(driver.title)
search = driver.find_element_by_id("search-keyword")
search.clear()
search.send_keys("爬虫")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "router-link-active"))
)
titles = driver.find_elements_by_class_name("title")
for title in titles:
    print(title.text)

link = driver.find_element_by_link_text(
    "Python爬虫编程基础5天速成（2021全新合集）Python入门+数据分析")
link.click()
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
time.sleep(1)
driver.close()

time.sleep(3)
driver.quit()
