from lxml import etree

#text = '<div>aaaaaa</div>'
#html = etree.HTML(text)
#print(html)
#ret = etree.tostring(html).decode('utf-8')
#print(ret)


text = etree.parse('text.html')
#ret = etree.tostring(text,pretty_print=True)#.decode('utf-8')
#print(ret)
#ret = text.xpath('//li[@class="li1"]')
ret = text.xpath('//li/@class"')
print(ret)