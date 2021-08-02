from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget

PATh = r"C:\Users\12158\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATh)
url = "https://wallhaven.cc/toplist"  # 打开的主网站
driver.get(url)
# toplist = driver.find_element_by_class_name("toplist")
# toplist.send_keys(Keys.RETURN)

# imgs = driver.find_elements_by_class_name("preview")

# for img in imgs:
#     img.click()
#     img = driver.find_element_by_id("wallpaper")
#     print(img.get_attribute("src"))

imgs = driver.find_elements_by_class_name("preview")  # 获取子页面数组
for img in imgs:
    img.click()  # 跳转子页面
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)  # 窗口切换到子页面
    # img = driver.find_element_by_id("wallpaper")
    img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wallpaper")))  # 子页面加载完成
    scale = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Crop & Scale Download")))
    scale.click()  # 单击选择下载大小
    scale1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="respicker-form"]/div/table/tbody/tr[3]/td[2]/label')))
    scale1.click()  # 单击1920 x 1080
    done = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "green")))
    done.click()  # 单击done
    download = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Continue")))
    download.click()  # 单击下载
    time.sleep(2)
    driver.close()  # 关闭子页面
    driver.switch_to_window(window_before)  # 跳转回主页面

# path = os.path.join("toplist")
# os.mkdir(path)
# photo = os.path.join(path, "toplist" + '.jpg')
# wget.download(img.get_attribute("src"), photo)
# driver.close()

# keyword = toplist
# path = os.path.join(keyword)
# os.mkdir(path)
# count = 0

# for img in imgs:
#     save_as = os.path.join(path, keyword + str(count) + 'jpg')
#     img.click()
#     window_before = driver.window_handles[0]
#     window_after = driver.window_handles[1]
#     driver.switch_to_window(window_after)
#     img = driver.find_element_by_id("wallpaper")
#     wget.download(img.get_attribute("src"), save_as)
#     driver.close()
#     count += 1
