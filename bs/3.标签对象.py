from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), features="lxml")

# 找到title的标签
print(f"title标签的对象:{type(soup.title)}")

# 打印title标签的名字
print(f"title标签的名字:{soup.title.name}")

# 也能修改文档的名字
# soup.title.name = "anthony"
# print(soup.anthony)

# 打印title标签的属性
print(f"body的内容:{soup.body}")

# 打印标签里的属性
print(f"标签里的全部属性:{soup.input.attrs}")
print(f"标签里的type属性:{soup.input['type']}")

# 修改标签里的属性值
soup.input["value"] = "anthony22222"
print(f"标签里的value属性:{soup.input['value']}")

# 删除标签里的属性值
del soup.input["name"]
print(f"标签里的全部属性,此时应该没有name的属性值了:{soup.input.attrs}")

# 往标签里添加
soup.input["newAttr"] = "新添加的属性值"
print(f"标签里的newAttr属性:{soup.input['newAttr']}")

# 多值属性
print(f"多值属性,可以找到属性的多个值:{soup.input['class']}")

# 可以遍历的字符串
print(f"可以遍历的字符串:内容是:{soup.h1.string} 类型是:{type(soup.h1.string)}")

# 注释和特殊字符串
print(f"找到注释:这有啥不一样:{soup.h2.string}")
print(f"找到注释:这有啥不一样:{type(soup.b.string)},{soup.b.string}")