import os
import shutil
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import wget
import path

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

driver = webdriver.Chrome(path.PATh)
url = "https://www.instagram.com/"
driver.get(url)

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")))
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
username.send_keys(path.username)
password.send_keys(path.password)
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
keyword = path.keyword
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(2)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD")))
for i in range(5):  # 页面下滑
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
# driver.execute_script("window.scrollTo(0, 0);")

imgs = driver.find_elements_by_class_name("FFVAD")

path = os.path.join("spider data", keyword)
if os.path.isdir(path):
    shutil.rmtree(path, True)
os.mkdir(path)

count = 0
num = 0
for img in imgs:
    save_as = os.path.join(path, keyword + '%d.jpg' % count)
    # print(img.get_attribute("src"))
    num += 1
    try:
        wget.download(img.get_attribute("src"), save_as)
    except Exception as e:
        print("发生错误", e, '\n', img.get_attribute("src"))
        continue
    count += 1
print("捕获数：", num)
driver.quit()
