from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

img = driver.find_elements_by_xpath('//*[id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()',img)
driver.save_screenshot('yincangbaidu.jpg')