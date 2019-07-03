from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Nexus 6'
# desired_caps['app'] = r'E:\1\34143aca0dc04db1ba48fc891839998e.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['noReset'] = True        #保留上次的参数

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)       #间隔5秒

def checkCancelBtn():
    print('check cancelBtn')
    try:
        cancelBtn=driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def checkShipBtn():
    print('check shipBtn')
    try:
        shipBtn=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no shipBtn')
    else:
        shipBtn.click()

checkCancelBtn()
checkShipBtn()
