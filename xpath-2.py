from lxml import etree
import urllib.request
import urllib.parse
import requests


#https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=0 第一页
#https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=50 第二页
#https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=100 第三页

#https://tieba.baidu.com/p/5785610924
index = 1
def save_img(img_url):
    global index
    file = open('./tiebaimg/'+str(index)+'.jpg','wb')

    #imgs = urllib.request.urlopen(img_url).read()    #方法一
    imgs = requests.get(img_url).content      #方法2

    file.write(imgs)
    file.close()
    index +=1

def load_img(loadurl):
    content = requests.get(loadurl).content
    html = etree.HTML(content) #转成xpath对象
    #print(html)
    img_list = html.xpath("//img[@class='BDE_Image']/@src")  #[@changedsize='true']加上后只看楼主图片
    #print(img_list)
    if img_list:
        for img_url in img_list:
            #print(img_url)
            save_img(img_url)

def load_page(url):
    content = requests.get(url).content #要转码
    #content = requests.get(url).text #不用转码
    print(content)
    html = etree.HTML(content)    #转成xpath对象
    #print(html)

    link_list = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    #print(link_list)
    for link in link_list:
        full_link = 'http://tieba.baidu.com'+link
        #print(full_link)
        load_img(full_link)


kw = '美女'  #input('请输入访问的贴吧')
b_page = 1   #int(input('请输入起始页'))
e_page = 1

for page in range(b_page,e_page+1):
    pn = (page-1)*50
    word = {'kw':kw,'pn':pn}
    base_url = 'http://tieba.baidu.com/f?'

    data = urllib.parse.urlencode(word)
    url = base_url + data
    print(url)
    load_page(url)
