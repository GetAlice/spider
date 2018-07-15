from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

soup = BeautifulSoup(html,'lxml')    #指定使用lxml解析器，不添加会报警但是不影响使用
#print(soup.prettify())    #格式化输出soup对象的内容
#print(soup.head.name)   #html的head，加name后输出head的name
#print(soup.body)   #html的body
#print(soup.a)       #html的a标签链接,只能查找到第一个
#print(soup.p)       #html的p标签,只能查找到第一个
#print(soup.p.attrs)  #p标签的属性，输出字典
#print(soup.p.get('class')) #输出p标签的class属性=什么
#print(soup.p.string)  #p的内容,不包括标签
#print(soup.a.string) #a的内容，但是注释掉后的内容会把注释符去掉显示内容
'''
print(soup.head)
print(soup.title)
print(soup.head.contents) #将head内容以列表的方式输出,包括标签
print(soup.p.b)
print(soup.p.b.contents)


print(soup.body.children)     #所有子节点,不是列表但是可以遍历
for each in soup.body.children:
    print(each)
'''
#print(soup.body.select())   #.+类名查找类的内容，#+id名查找ID内容

#print(soup.find_all('p',{属性名称:属性内容}))   #找到所有的p标签
tag_list = soup.find_all(['a','b'])   #找到所有的a和b标签
print(tag_list)



#soup_1 = BeautifulSoup(open('text.html'),'lxml')
#print(soup_1)
