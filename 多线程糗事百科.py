import requests
import threading
import json
import queue
from lxml import etree


lock = threading.Lock()

CRAW_EXIT=False
PARSE_EXIT=False

class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename,lock):
        super(ThreadParse,self).__init__()
        self.threadName =threadName
        self.dataQueue=dataQueue
        self.filename=filename
        self.lock = lock
    def run(self):
        print('启动',self.threadName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                #print(html)
                self.parse(html,self.filename)
            except:
                pass
        print('结束'+self.threadName)

    def parse(self,html,filename):
        html = etree.HTML(html)
        ret = html.xpath('//div[contains(@id,"qiushi_tag")]')
        # print(ret)

        i = 0
        items = []
        for site in ret:
            item = {}
            imageUrl = site.xpath('./div//@src')[0]
            imageUrl = 'http:' + imageUrl
            # print(imageUrl)
            username = site.xpath('.//h2')[0].text.strip()
            # print(username)
            content = site.xpath('.//div[@class="content"]/span/text()')  # .text因为内容有br，只会取第一行，所以在xpath里用text(),出来的是列表
            content2 = ''
            for each in content:
                str1 = each.replace('\n', '').replace(' ', '')
                content2 += str1
            # print(content)
            vote = site.xpath('.//div//li[@class="up"]//span')[0].text
            # print(vote)
            comment = site.xpath('.//div/span/a/i[@class="number"]')[0].text
            # print(comment)
            item['头像链接'] = imageUrl
            item['用户名'] = username
            item['内容'] = content2
            item['点赞数'] = vote
            item['评论数'] = comment
            print(item)
            json_obj = json.dumps(item, ensure_ascii=False)
            json_obj += "\n\n"
            while self.lock:
                filename.write(json_obj)


            items.append(item)

class ThreadCraw(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCraw,self).__init__()     #调用父类初始化
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    def run (self):

        while not CRAW_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
                content = requests.get(url,headers=self.header).text
                self.dataQueue.put(content)
            except:
                pass
        print('结束'+self.threadName)

def main():

    pageQueue = queue.Queue(10) #创建10个队列

    for i in range(1,11):
        pageQueue.put(i)

    dataQueue = queue.Queue()
    crawList = ['采集线程1','采集线程2','采集线程3']

    threadcraw = []
    for threadName in crawList:
        thread = ThreadCraw(threadName,pageQueue,dataQueue)
        thread.start()
        print('启动线程:',threadName)
        threadcraw.append(thread)

    while not pageQueue.empty():
        pass
    global CRAW_EXIT
    CRAW_EXIT = True
    print('pageQueue为空')

    for thread in threadcraw:
        thread.join()
        print('主线程结束，等待所有线程结束成功')




    filename = open('m_qiushi.txt', 'a')
    parseList = ['解析线程1', '解析线程2', '解析线程3']
    threadparse = []
    for threadName in parseList:
        thread =ThreadParse(threadName,dataQueue,filename,lock)
        thread.start()
        print('启动',threadName)
        threadparse.append(thread)

        while not dataQueue.empty():
            pass
        global PARSE_EXIT
        PARSE_EXIT = True
        for thread in threadparse:
            thread.join()
            print('解析线程结束，等待所有线程结束成功')

        with lock:
            filename.close()
if __name__ == '__main__':
    main()