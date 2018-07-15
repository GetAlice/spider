import requests
import urllib.parse
import json
import urllib3



def get_page_index(offset,keyword):
    data={
    'autoload':'true',
    'count':20,
    'cur_tab':1,
    'format':'json',
    'from':'search_tab',
    'keyword':keyword,
    'offset':offset
    }
    url = 'https://www.toutiao.com/search_content/?' + urllib.parse.urlencode(data)
                 #urllib或requests在打开https站点是会验证SSL证书。
                 #如果没有证书将会报错,简单的处理办法是在get方法中加入verify参数，并设为false。
                 #但是取消验证SSL会弹出警报，虽然不影响使用，但还是能用urllib3.disable_warnings()将警报去掉
    urllib3.disable_warnings()
    res = requests.get(url,verify=False)
    #print(url)
    #print(res.text)
    if res.status_code==200:    #如果状态码等于200ok
        return res.text
    return None

def parse_page_index(html):
    data = json.loads(html)   #读取json数据
    #print(data)
    #print(data.keys())
    #print(data.values())
    for item in data.get('data'):
        yield(item.get('share_url'))


if __name__ == '__main__':
    html = get_page_index(20,'街拍')
    parse_page_index(html)