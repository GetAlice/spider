import urllib.request
import urllib.parse
import json
import time
import random
import hashlib
import json

'''
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'    #_o是url复制下来的，有的话会出错,

D = "ebSeFb%=XZ%T[KZ)c(sy!"
S = "fanyideskweb"

def get_salt():
    salt = int(time.time()*1000)+random.randint(0,10) #js看到的salt公式
    return str(salt)

def get_md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()

def get_sigh(msg):
    sign = S + msg + get_salt() + D
    return get_md5(sign)

def get_fromdata(msg):
    salt = get_salt()
    sign = get_sigh(msg)
    fromdata = {
        "i":msg,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":sign,
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }
    return fromdata

if __name__ == '__main__':
    while True:
        msg = input('请输入要翻译的单词')
        if msg == 'q':
            break
        else:
            fromdata = get_fromdata(msg)
            data = urllib.parse.urlencode(fromdata).encode('utf-8')
            headers = {'User-Agent':'aaa'}
            req = urllib.request.Request(url,data=data,headers=headers)
            res = urllib.request.urlopen(req)
            #res = urllib.request.urlopen(url,data)
            html = res.read().decode('utf-8')
            target = json.loads(html)
            print('result:%s'%target['translateResult'][0][0]['tgt'])
'''

