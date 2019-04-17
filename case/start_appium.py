#coding=utf-8
from appium import webdriver

capabilities = {
	"platformName": "Android",
  	"deviceName": "127.0.0.1:21503",
  	"app": "F:\\mukewang.apk",
	# "appPackage":"",
	# "appActivity":"",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)

import time
time.sleep(2)
driver.swipe(500,400,50,400,1000)
time.sleep(2)
driver.swipe(500,400,50,400,1000)
time.sleep(3)
