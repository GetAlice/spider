import urllib.request
import requests
from lxml import etree
import base64

header = {
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding: gzip, deflate',
    'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control: max-age=0',
    'Connection: keep-alive',
    'Cookie: _ga=GA1.2.1555792799.1531015096; _gid=GA1.2.1862211856.1531122933; _gat_gtag_UA_462921_3=1',
    'Host: jandan.net',
    'Upgrade-Insecure-Requests: 1'
    'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}




index = 1

def saveimg(img_url):
    global index
    if 'jpg' in img_url:
        img_file = open('./jiandanimg/'+'煎蛋网'+str(index)+'.jpg','wb')
    else:
        if 'gif' in img_url:
            img_file = open('./jiandanimg/'+str(index)+'.gif','wb')

    img = requests.get(img_url).content
    img_file.write(img)
    img_file.close()
    index += 1

startpage = 227
endpage = 227

for page in range(startpage,endpage+1):
    url = 'http://jandan.net/pic/page-'+str(page)+'#comments'
    res = requests.get(url,verify=False)

    #print(res.content)
    context = res.content #requests.get(url).content
    html = etree.HTML(context)

    #查看网页代码的时候发现网站为了防止爬取，将图片网址转成base64暗码放在了span中
    img_list = html.xpath('//li//div//p/span[@class="img-hash"]') #.text
    name_list = html.xpath('//li//div//strong')
    dic = {}
    lis = []
    for n in name_list:
        username = n.text

        for i in img_list:
            #print(i.text)
            i_base64 = i.text
            i_str = base64.b64decode(i_base64).decode('utf-8')    #因为base64解码后会变成b字节，所以要转码成str
            img_url = 'http:'+i_str

            #saveimg(img_url)
        dic[username] = img_url
        lis.append(dic)
        dic = {}
    print(lis)

