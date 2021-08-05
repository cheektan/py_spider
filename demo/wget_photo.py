import wget
import urllib
import os

# UA
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')]
urllib.request.install_opener(opener)

# wget.download(
#     "https://w.wallhaven.cc/full/o3/wallhaven-o31jy9.jpg")
# wget.download(
#     "https://www.sciencedirect.com/science/article/pii/S002202480302267X/pdfft?md5=3a43f2b8e4e1b9762d8906f2270b388d&pid=1-s2.0-S002202480302267X-main.pdf")

filename = os.path.join("spider data", "paper.pdf")
urllib.request.urlretrieve(
    "https://www.sciencedirect.com/science/article/pii/S002202480302267X/pdfft?md5=3a43f2b8e4e1b9762d8906f2270b388d&pid=1-s2.0-S002202480302267X-main.pdf", filename)
