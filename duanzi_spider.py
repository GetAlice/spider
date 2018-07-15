import urllib.request
import urllib.parse
import re

class Spider:
    def loadPage(self,page):
        url = 'https://www.neihan8.com/article/list_5_'+page+'.html'

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
        req = urllib.request.Request(url,headers=header)
        res = urllib.request.urlopen(req)
        html = res.read().decode('gb2312')
        #print(html)
        patt = re.compile(r'<div class="f18 mb20">(.*?)</div>',re.S) #re.S作为一个整体匹配
        item_list = patt.findall(html)
        #print(item_list)
        for item in item_list:
            #print('*'*50)
            #print(item.strip().replace('<p>','').replace('</p>','').replace('<br />','').replace('&ldquo;',''))
            text = item.strip().replace('<p>','').replace('</p>','').replace('<br />','').replace('&ldquo;','')
            text = text.replace('&hellip;','').replace('&rdquo;','')
            self.save_file(text)

    def save_file(self,text):
        file = open('duanzi.txt','a')
        file.write(text)
        file.write('\n'*2)
        file.write('='*50)
        file.write('\n')
        file.close()

if __name__ == '__main__':
    page = input('请输入第几页:')
    myspider = Spider()
    myspider.loadPage(page)