from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("index.html"), features="lxml")

# find


# find_all()
for one in soup.find_all("input"):
    print(one)

# find_all() 正则表达式
for one in soup.find_all(re.compile("^input")):
    print(one)

for one in soup.find_all(["h1", "input"]):
    print(one)


def test_method(tag):
    return tag.has_attr("class") and not tag.has_attr("id")


print(soup.find_all(test_method))
