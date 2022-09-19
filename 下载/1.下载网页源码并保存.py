import requests

url = "https://www.google.com/search?q=ceshi"

response = requests.get(url)
print(response.content)

file = open("../下载网页源码并保存/index.html", "wb")
file.write(response.content)
file.close()
