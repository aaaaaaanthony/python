from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), features="lxml")

# 完整打打印html文档
# print(soup.prettify())

# 打印html的title
print(soup.title)

# 打印html的title的标签的名字
print(soup.title.name)

# 打印html的title的父节点的标签的名字
# TODO 是直接上级还是祖父?
print(soup.title.parent.name)

# 打印html的title的标签里的值
print(soup.title.string)

print(soup.span)