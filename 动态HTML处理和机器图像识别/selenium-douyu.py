#https://www.douyu.com/directory/all

from selenium import webdriver
from bs4 import BeautifulSoup
import unittest

drive = webdriver.Chrome()
drive.get('http://www.douyu.com/directory/all')
#print(drive.page_source.find('shark-pager-disable-next'))
#print(drive.page_source.find('shark-pager-next'))
while True:
    soup = BeautifulSoup(drive.page_source,'lxml')
    names = soup.find_all('h3',{'class':'ellipsis'})
    nums = soup.find_all('span',{'class':'dy-num fr'})

    for name,num in zip(names,nums):
        print('观众人数:'+num.get_text(),'\t\t房间名:'+name.get_text().strip())

    if drive.page_source.find('shark-pager-disable-next') != -1:
        break
    drive.find_element_by_class_name('shark-pager-next').click()
    print('下一页')