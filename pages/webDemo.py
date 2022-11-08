from selenium import webdriver
from common.keys import Testkeys
from time import sleep
from location.index import index
driver = Testkeys('chrome','http://www.baidu.com')
driver.input_text('id',index.search,'测试')
driver.click('id','su')