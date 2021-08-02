import wget
import urllib

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

wget.download(
    "https://w.wallhaven.cc/full/o3/wallhaven-o31jy9.jpg")
