import urllib.request
import urllib.parse

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/60.0'
}

url = 'http://www.baidu.com/s'
word = {'wd':'大数据档案'}
word = urllib.parse.urlencode(word)     #将搜索的字符串转码

urllib.parse.unquote('wd=%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%A1%A3%E6%A1%88')   #转成原来搜索的字符串

new_url = url+ '?' + word
print(new_url)

req = urllib.request.Request(new_url,headers=header)
res = urllib.request.urlopen(req)

data = res.read().decode('utf-8')
print(data)