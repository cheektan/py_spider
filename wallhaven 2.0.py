from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget
import urllib.request

PATh = r"C:\Users\12158\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATh)

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

# 打开的主网站
url = "https://wallhaven.cc/search?categories=111&purity=110&ratios=16x9&topRange=1M&sorting=hot&order=desc"
keyword = "hot"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "preview")))

for i in range(2):  # 页面下滑
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

imgs = driver.find_elements_by_class_name("loaded")  # 获取子页面数组
count = 0
path = os.path.join(keyword)
os.mkdir(path)

for img in imgs:
    url = img.get_attribute("src")
    url0 = url[:33] + 'wallhaven-' + url[33:]
    url1 = url0.replace("th", "w", 1)
    url2 = url1.replace(" ", "")
    url_rep = url2.replace("small", "full", 1)
    photo = os.path.join(path, str(count) + '.jpg')
    try:
        wget.download(url_rep, photo)
    except IOError:
        url_rep1 = url_rep.replace("jpg", "png")
        wget.download(url_rep1, photo)
    # print(url_rep)
    count += 1
