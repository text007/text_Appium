from appium import webdriver
import time

desired_caps = dict()
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0.1"
desired_caps["deviceName"] = "127.0.0.1:7555"
desired_caps["appPackage"] = "org.cocos2dx.FlowerPower"
desired_caps["appActivity"] = ".javascript.AppActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)

driver.quit()
