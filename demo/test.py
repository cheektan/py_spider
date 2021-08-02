

# https: // wallhaven.cc/w/8oky1j
# https: // w.wallhaven.cc/full/8o/wallhaven-8oky1j.jpg
url = "https: // th.wallhaven.cc/small/8o/8oky1j.jpg"

url0 = url[:35] + 'wallhaven-' + url[35:]
url1 = url0.replace("th", "w", 1)
url2 = url1.replace(" ", "")
url_rep = url2.replace("small", "full", 1)
print(url_rep)


# s = 'abcdefghij'

# print(s[:4] + 'XXX' + s[7:])
# # abcdXXXhij

# s_replace = 'XXX'
# i = 4
# print(s[:i] + s_replace + s[i + len(s_replace):])
# # abcdXXXhij

# print(s[:4] + '-' + s[7:])
