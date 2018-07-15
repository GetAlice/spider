from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import ssl

context = ssl._create_unverified_context()  #消除ssl报警

def tecent(page):
    global context
    url = 'http://hr.tencent.com/position.php?&start='+str(page*10)+'#a'
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req,context=context)
    html = res.read().decode('utf-8')
    #print(html)

    soup = BeautifulSoup(html,'lxml')
    ret_even = soup.select('tr[class="even"]')
    ret_odd = soup.select('tr[class="odd"]')
    '''print(ret_even)
    print('*'*50)
    print(ret_odd)
    print('*' * 50)'''

    ret = ret_even + ret_odd
    items = []
    for site in ret:
        item = {}
        #print(site)                #td下的a  .get_text()也可以
        Position_name = site.select('td a')[0].string
        Position_link = site.select('td a')[0].attrs['href']   #取属性的href
        #print(site.select('td a')[0].attrs)
        Position_cat = site.select('td')[1].string
        Position_num = site.select('td')[2].string
        Position_location = site.select('td')[3].string
        Position_pub = site.select('td')[4].string
        #print(Position_pub)
        item['职位名称'] = Position_name
        item['职位链接'] = Position_link
        item['职位类别'] = Position_cat
        item['职位人数'] = Position_num
        item['职位地点'] = Position_location
        item['发布日期'] = Position_pub
        items.append(item)
    for each in items:
        print(each)

for i in range(10):

    tecent(i)
