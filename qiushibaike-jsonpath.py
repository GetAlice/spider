#//div[contains(@id,"qiushi_tag")]
import urllib.request
import re
import requests
from lxml import etree
import json
import jsonpath

page = 1
url = 'http://www.qiushibaike.com/8hr/page/'+str(page)

res = requests.get(url)
res_html = res.text
#print(res_html)
####################### 下面注释代码效果一样
'''
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
res_html = res.read().decode('utf-8')     #本来是bytes字节,要换回字符串
'''

html = etree.HTML(res_html)
#print(html)
ret = html.xpath('//div[contains(@id,"qiushi_tag")]')
#print(ret)

i=0
items = []
for site in ret:
    item = {}
    imageUrl = site.xpath('./div//@src')[0]
    imageUrl = 'http:' + imageUrl
    #print(imageUrl)
    username = site.xpath('.//h2')[0].text.strip()
    #print(username)
    content = site.xpath('.//div[@class="content"]/span/text()')#.text因为内容有br，只会取第一行，所以在xpath里用text(),出来的是列表
    content2 = ''
    for each in content:
        str1 = each.replace('\n','').replace(' ','')
        content2 += str1
    #print(content)
    vote = site.xpath('.//div//li[@class="up"]//span')[0].text
    #print(vote)
    comment = site.xpath('.//div/span/a/i[@class="number"]')[0].text
    #print(comment)
    item['头像链接'] = imageUrl
    item['用户名'] = username
    item['内容'] = content2
    item['点赞数'] = vote
    item['评论数'] = comment
    print(item)
    json_obj = json.dumps(item,ensure_ascii=False)
    json_obj += "\n\n"
    with open('qiushibaike1.json', 'a') as f:
        f.write(json_obj)


    items.append(item)
#print(items)
'''

json_obj = json.dumps(items,ensure_ascii=False)

with open('qiushibaike.json','w') as f:
    #f.write(json_obj)
    json.dump(json_obj,f)
'''
