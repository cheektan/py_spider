from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget
import urllib.request
import path

driver = webdriver.Chrome(path.PATh)

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

url = "https://wallhaven.cc/search?categories=110&purity=110&atleast=1920x1080&ratios=16x9&sorting=favorites&order=desc"  # 打开的主网站
keyword = "favorites"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "preview")))

for i in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

imgs = driver.find_elements_by_class_name("preview")  # 获取子页面数组
count = 0
path = os.path.join("spider data", keyword)
os.mkdir(path)

for img in imgs:
    img.click()
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    img = driver.find_element_by_id("wallpaper")
    photo = os.path.join(path, str(count) + '.jpg')
    wget.download(img.get_attribute("src"), photo)
    driver.close()
    driver.switch_to_window(window_before)
    count += 1
