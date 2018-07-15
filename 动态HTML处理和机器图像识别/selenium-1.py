from selenium import webdriver
import time
#自动处理
drive = webdriver.Chrome()  #没加环境变量直接写目录路径
#drive.get('http://www.baidu.com')   #自动输入网址
#drive.find_element_by_id('kw').send_keys('美女')  #找到百度搜索框ID=kw，在搜索框输入XX
#drive.find_element_by_id('su').click()           #找到搜索按钮，点击搜索按钮
#drive.save_screenshot('baidu.png')

drive.get('http://www.douban.com')
drive.find_element_by_id('form_email').send_keys('13537656018')
drive.find_element_by_id('form_password').send_keys('cnm.dhg.1997')
drive.find_element_by_class_name('bn-submit').click()
drive.save_screenshot('登陆成功.png')
'''
html = drive.page_source
f = open('登陆成功.html','w',encoding='utf-8')
f.write(html)
f.close()
'''

with open('登陆成功.html','w',encoding='utf-8') as f:
    f.write(drive.page_source)    #返回登陆成功后的页面代码写入文件

time.sleep(2)

drive.quit()



