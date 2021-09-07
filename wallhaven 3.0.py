from os import name
from bs4 import BeautifulSoup  # 解析网页
import requests as req

proxies = {
    "http": "http://127.0.0.1:11223",
    "https": "http://127.0.0.1:11223",
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

origin_url = 'https://wallhaven.cc/search?categories=110&purity=100&atleast=1920x1080&ratios=16x9&topRange=1M&sorting=toplist&order=desc&page='

for page in range(1, 11):  #  抓取网站页数
  url = origin_url + str(page)  #  第几页网址
  r = req.get(url, proxies=proxies, headers=headers)  #  获取网址html
  soup = BeautifulSoup(r.text, 'lxml')  #  分析网址纯文本html
  soup_index = soup.find_all("img")  # 查找img图片标签
  i = 1
  for index in soup_index:  #  抓取所有img图片标签
    img_url = index.get('data-src')  # 逐个提取img标签中的src部分
    if img_url is not None:  #  去除None的链接
      img_url = img_url[:33] + 'wallhaven-' + img_url[33:]
      img_url = img_url.replace("th", "w", 1)
      img_url = img_url.replace(" ", "")
      img_url = img_url.replace("small", "full", 1)
      img = req.get(img_url, headers=headers, proxies=proxies)  #  获取原始图片直链
      if img.status_code == 404:  #  修正404网址
        img_url = img_url.replace("jpg", "png")
        img = req.get(img_url, headers=headers, proxies=proxies)
      # print(img.status_code)
      name = "./spider data/V3.0/第" + str(page) + "页" + "第" + str(i) + "张" + ".jpg"
      i += 1
      with open(name, mode='wb') as file:  #  保存图片
        file.write(img.content)
