from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), features="lxml")

# 获取title
print(soup.title)
print(type(soup.title))

# 获取h1标签
print(soup.h1)

# 获取h1标签的名称
print(f'{soup.h1.name} 标签的对象是:,{type(soup.h1.name)}')

# 获取h1标签的属性
print(f'标签里的属性有这些:{soup.h1.attrs}')
print(f'标签里的value是:{soup.h1.string}')

# 嵌套
print(f"嵌套查询:{soup.head.title.string}")

# 关联选择
print(f"获取子节点的信息:{soup.div.contents}")
# 获取div节点的子节点
# 0 是当前元素
for i, child in enumerate(soup.div.children):
    print(f"索引:{i},{child}")

# 获取父节点
print(f"获取父节点:{soup.h1.parent}")
print(f"获取祖先节点:{soup.h1.parents}")

# 获取兄弟节点
print(f"获取兄弟节点:{list(enumerate(soup.h1.previous_siblings))}")

# css选择器
soup.select()