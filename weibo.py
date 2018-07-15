import requests
import urllib.request
import urllib3
import json
import urllib.parse
import pyquery

#网页请求头有X-Requested-With: XMLHttpRequest说明是ajax
# ajax url
# https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=1076032830678474&type=uid&value=2830678474&containerid=1076032830678474&page=1&standalone=0
# https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=1076032830678474&type=uid&value=2830678474&containerid=1076032830678474&page=2&standalone=0
# https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=1076032830678474&type=uid&value=2830678474&containerid=1076032830678474&page=3&standalone=0
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host':'m.weibo.cn',
        'Referer':'https://m.weibo.cn/u/2830678474',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/64.0.3282.186 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'

}

urllib3.disable_warnings()

def get_page(page):
    param = {
        'uid': '2830678474',
        'luicode': '10000011',
        'lfid': '1076032830678474',
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page,
        'standalone': '0',

    }
    base = urllib.parse.urlencode(param)
    url = base_url + base
    #print(url)
    # urllib或requests在打开https站点是会验证SSL证书。
    # 如果没有证书将会报错,简单的处理办法是在get方法中加入verify参数，并设为false。
    # 但是取消验证SSL会弹出警报，虽然不影响使用，但还是能用urllib3.disable_warnings()将警报去掉
    res = requests.get(url,headers=headers,verify=False)

    if res.status_code==200:
        return res.json()
    return None

def parse_page(json):
    if json:
        items = json['data']['cards']
        #print(items)
        for item in items:
            if item['card_type'] !=9:
                continue
            #print(item)
            each = item['mblog']
            weibo={}
            #weibo[id] = item['id']
            weibo['用户名'] = each['user']['screen_name']
            weibo['内容'] = pyquery.PyQuery(each['text']).text() #去掉正文中的HTML标签
            weibo['发表时间'] = each['created_at']
            weibo['点赞数'] = each['attitudes_count']
            weibo['转发数'] = each['reposts_count']
            weibo['评论数'] = each['comments_count']
            print(weibo)

data = get_page(1)
parse_page(data)
