from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), features="lxml")

# 找到所有input
print(soup.find_all("input"))
