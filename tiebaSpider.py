#爬百度贴吧 前10页
'''
https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0     第一页
https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50    第二页
https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100   第三页
'''
import urllib.request
import urllib.parse
import os
print(os.getcwd())

'''
def loadPage(url,filename):
    print('正在下载',filename)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/60.0'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    data = res.read()  #.decode('utf-8')
    print(data)

    return data

def writePage(html,file_name):
    print('正在写入文件')
    with open(file_name,'wb') as f:
        f.write(html)
    print('*'*50)


def tiebaSpider(url,beginpage,endpage):
    for page in range(beginpage,endpage+1):  #因为左闭右开，所以endpage+1
        pn = (page-1)*50
        file_name = '第' + str(page) + '页'
        fullurl = url + '&pn=' + str(pn)    # http://tieba.baidu.com/f?(kw=xxxxx)&pn=(页数)
        print(fullurl)

        html = loadPage(fullurl,file_name)
        writePage(html,file_name)



if __name__ == '__main__':
    #kw = 'lol'      #input('请输入要爬的贴吧名')
    kw = {'kw':'lol'}

    begin_page = 1  #int(input('请输入起始页'))
    end_page = 3    #int(input('请输入结束页'))

    url = 'http://tieba.baidu.com/f?'
    key = urllib.parse.urlencode(kw)

    newurl = url + key
    tiebaSpider(newurl, begin_page, end_page)
'''


'''
def loadpage(fullurl,filename):
    heard = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/60.0'}
    print('正在下载')
    req = urllib.request.Request(fullurl,headers=heard)
    res = urllib.request.urlopen(req)
    data = res.read()
    return data

def writepage(html,filename):
    print('正在写入')
    with open(filename,'wb') as file:
        file.write(html)
    print('*'*50)


def tiebaSpider(newurl,startpage,endpage):
    for page in range(startpage,endpage+1):
        pagenum = (page-1)*50
        filename = '第'+str(page)+'页.html'
        fullurl = newurl + '&pn=' + str(pagenum)
        print(fullurl)
        html = loadpage(fullurl,filename)
        writepage(html,filename)



if __name__ == '__main__':
    kw = {'kw':'lol'}
    url = 'http://tieba.baidu.com/f?'

    key = urllib.parse.urlencode(kw)
    newurl = url + key
    startpage = 1
    endpage = 5
    tiebaSpider(newurl,startpage,endpage)
'''

def loadpage(fullurl,filename):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/60.0'}
    print('正在下载'+filename)
    req = urllib.request.Request(fullurl,headers=header)
    res = urllib.request.urlopen(req)
    data = res.read()
    print(data)
    return data

def writepage(html,filename):
    with open(filename,'wb') as file:
        file.write(html)
        print('正在写入'+filename)

def tiebaSpider(newurl,startpage,endpage):
    for page in range(startpage,endpage+1):
        urlpage = (page-1)*50
        fullurl = newurl + '&pn=' + str(urlpage)
        filename = '海鱼吧第'+str(page)+'页.html'
        print(fullurl)
        html = loadpage(fullurl,filename)
        writepage(html,filename)

if __name__ == '__main__':
    kw = {'kw':'海鱼'}
    url = 'http://tieba.baidu.com/f?'
    key = urllib.parse.urlencode(kw)

    newurl = url + key
    startpage = 1
    endpage = 3
    tiebaSpider(newurl,startpage,endpage)