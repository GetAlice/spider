#做实验的时候不能打开fidder，会影响
import urllib.request

#res = urllib.request.urlopen("http://www.taobao.com")     #不能构造http的头
'''
print(type(res))
html = res.read().decode('utf-8')
print(html)
'''

url = 'http://www.baidu.com'
#构造一个User-Agent头
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/60.0'
}

#url 连同 headers，一起构造Request请求，这个请求将附带浏览器的User-Agent
req = urllib.request.Request(url,headers=header)
req.add_header('Connection','keep-alive')
print(req)
# 向服务器发送请求
res = urllib.request.urlopen(req)
print(type(res))

#类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串,如果不用decode转码返回的全是\n\r
html = res.read().decode('utf-8')
print(html.encode('utf-8'))

code = res.getcode()
print(code)

print(res.geturl())
print(res.info())



