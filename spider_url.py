import urllib.request
import requests
import os

url = "https://w.wallhaven.cc/full/rd/wallhaven-rdymmm.jpg"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
# url = urllib.request.Request(url, headers=headers)
# urllib.request.urlopen(url).read()


opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)
# urllib.request.urlretrieve(URL, path)

path = os.path.join("wallhaven")
# os.mkdir(path)
filename = '{}{}{}{}'.format(path, os.sep, "1", ".jpg")
# urllib.request.urlretrieve(
# "https://w.wallhaven.cc/full/rd/wallhaven-rdymmm.jpg", filename=filename)
urllib.request.urlretrieve(url, filename=filename)
