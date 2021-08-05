from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import path
import wget


driver = webdriver.Chrome(path.PATh)

driver.get("https://www.sciencedirect.com/")

search = driver.find_element_by_xpath(
    '//*[@id="qs-searchbox-input"]')
search.clear()
search.send_keys("SiC Growth")
search.send_keys(Keys.RETURN)

# check = driver.find_element_by_xpath(
#     '//*[@id="srp-toolbar"]/div[1]/div[1]/div/label/span[1]')
check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="srp-toolbar"]/div[1]/div[1]/div/label/span[1]')))
check.click()
download = driver.find_element_by_class_name("download-all-link-text")
download.click()

driver.quit()
