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
import shutil

driver = webdriver.Chrome(path.PATh)

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

# 打开的主网站
url = "https://wallhaven.cc/search?categories=110&purity=100&atleast=1920x1080&ratios=16x9&topRange=1M&sorting=toplist&order=desc"
keyword = "toplist"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "preview")))

for i in range(5):  # 页面下滑
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
# time.sleep(2)

imgs = driver.find_elements_by_class_name("loaded")  # 获取子页面数组
count = 0
path = os.path.join("spider data", keyword)
# os.mkdir(path)
if os.path.isdir(path):
    shutil.rmtree(path, True)
os.mkdir(path)

for img in imgs:
    url = img.get_attribute("src")
    url0 = url[:33] + 'wallhaven-' + url[33:]
    url1 = url0.replace("th", "w", 1)
    url2 = url1.replace(" ", "")
    url_rep = url2.replace("small", "full", 1)
    photo = os.path.join(path, str(count) + '.jpg')
    # if os.path.exists(photo):
    #     os.remove(photo)
    try:
        wget.download(url_rep, photo)
    except IOError:
        url_rep1 = url_rep.replace("jpg", "png")
        # wget.download(url_rep1, photo)
        try:
            wget.download(url_rep1, photo)
        except Exception as e:
            print("发生错误", e, '\n', url_rep1)
            continue
    # print(url_rep)
    count += 1
print("\n捕获数：", count)
driver.quit()
