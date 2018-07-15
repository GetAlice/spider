import urllib.parse
import requests
import urllib3
from lxml import etree
import time
import random

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            'upgrade-insecure-requests': '1',
            'cookie':'__cfduid=d408e02231fb9b154ab9c2fbf637da8801529925740; Hm_lvt_bf527c8e99a212fc0d7f77228e7bee30=1531289096; PHPSESSID=jtf299c18egmp5lu43mr0sasvp; Hm_lpvt_bf527c8e99a212fc0d7f77228e7bee30=1531294764'
           }

sousuoneirong = ['死侍2'] #input('输入搜索内容').split(',')

def spider_data(newlink):
    #print(headers)
    pro = ['180.76.111.69:3128','180.97.193.58:3128']
    content = requests.get(newlink,headers=headers,proxies={'https':random.choice(pro)}).content

    html = etree.HTML(content)
    name = html.xpath('//div[@class="inerTop"]/div[@class="panel panel-primary"]//h3//div[@class="text-left"]')[0].text.strip()
    magnet = html.xpath('//textarea')[0].text.strip()
    print('片名:'+name,'\n磁力:'+magnet)
def spider(data):
    global headers
    url = 'http://zhongzijun.com/list/' + data + '/1'
    res = requests.get(url,headers=headers)
    headers['referer']='https://zhongzijun.com/list/' + data + '/1'
    if res.status_code == 200:
        print('正在查找，请稍等....')
        html = etree.HTML(res.content)
        link_list = html.xpath('//table[@class="table table-bordered table-striped"]//h4/a/@href')  # .text
        #print(link_list)
        for link in link_list:
            newlink = 'http://www.zhongziso.com'+link
            spider_data(str(newlink))
    else:
        print('查找内容出错或服务器出错')
        return None



for neirong in sousuoneirong:

    # urllib.parse.urlencode只能对字典编码，如果是字符串要用quote
    data = urllib.parse.quote(neirong)
    spider(data)

