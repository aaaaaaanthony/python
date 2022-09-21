from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), features="lxml")

# 找到所有input
# print(soup.find_all("input"))

# .contents 用法
print(soup.head)

print(soup.head.contents)

# children的用法
for child in soup.head.children:
    print(f"子节点:{child}")
print(f"child的节点有:{len(list(soup.head.children))}个")
print("=" * 40)

# descendants的用法,标签里的值也当做一个节点
for child in soup.head.descendants:
    print(f"子节点:{child}")
print(f"descendants的节点有:{len(list(soup.head.descendants))}个")

# string方法
print(f"string的用法:{soup.title.string}")
print(f"string的用法:{soup.html.string}")

# strings方法
for string in soup.title.strings:
    print(string)

# parent,看着像是直接父节点
print(f"父节点:{soup.title.parent}")
print(f"父节点:{soup.title.string.parent}")

# parents
for one in soup.input.parents:
    print(f"parents节点:{one.name}")

# 兄弟节点next_sibling,previous_sibling  这两个纯属有毒
print(f"兄弟节点next_sibling:{soup.h1.next_sibling}")
print(f"兄弟节点next_sibling:{soup.h1.next_sibling.next_sibling}")
print(f"兄弟节点previous_sibling:{soup.h2.previous_sibling}")
print(f"兄弟节点previous_sibling:{soup.h2.previous_sibling.previous_sibling}")

# .next_siblings 和 .previous_siblings
for one in soup.h1.next_siblings:
    print(one)
print("#" * 40)
for one in soup.p.previous_siblings:
    print(one)
