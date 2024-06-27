from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">最后一个p标签</p>
</body>

"""
#创建 Beautiful Soup对象,并设置用lxml解析器
soup = BeautifulSoup(html,"lxml")
#打开本地 HTML 文件的方式来创建对象
# soup = BeautifulSoup(open('hello.html'),"lxml")
#格式化输出 soup 对象的内容
print(soup.prettify())
print(type(soup))#<class 'bs4.BeautifulSoup'>
print(type(soup.name))# <class 'str'>
print(soup.name) # [document]
print(soup.attrs) # 文档本身的属性为空{}

print(soup.title)# <title>The Dormouse's story</title>
print(soup.head)# <head><title>The Dormouse's story</title></head>
print(soup.a)# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.p)# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print(type(soup.p))# <class 'bs4.element.Tag'>
print(type(soup.a))
print(type(soup.head))
print(type(soup.title))

print(soup.p.string)# The Dormouse's story
print(type(soup.p.string))#  <class 'bs4.element.NavigableString'>

list_a = soup.find_all(name="a")
for a in list_a:
   print(a.string)

print(soup.a.string)
print(type(soup.a.string))
print(soup.a.text)
print(type(soup.a.text))

print(soup.head.contents)
print(soup.head.contents[0])

for a in soup.find_all(name ="a"):
    contents = a.contents
    print(contents)

print(soup.body.children)#<listiterator object at 0x7f71457f5710>
for child in soup.body.children:
    print(child)

print("#"*20)

for child in soup.p.descendants:
    print(child)

list_p = soup.find_all(name="p")
for p in list_p:
   print(p.name,":的所以后代==============")
   for child in p.descendants:
      print(child)

print(soup.head.string)#The Dormouse's story
print(soup.title.string)#The Dormouse's story

#匹配所以b开头的标题它们是:body标签和b标签
for tag in soup.find_all(re.compile(r"^b")):
    print(tag.name)# body# b

for tag in soup.find_all(href=re.compile(r"http")):
    print(tag)

print(soup.find_all(["a", "b"]))

print(soup.find_all(id='link2'))

print(soup.find_all(text="Elsie"))

print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))

print(soup.find_all(text=re.compile("Dormouse")))

links = soup.find_all(href=re.compile(r'http://example.com/'))
#得到所以的链接
for link in links:
   print(link["href"])

print(soup.select('.sister'))

tags = soup.select(".story > .sister")
for tag in tags:
   print(tag)

print(soup.select('#link1'))

print(soup.select('p #link1'))

print(soup.select("head > title"))