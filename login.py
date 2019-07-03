from kyb.capability import driver,NoSuchElementException

#登录方法
def login():
    # 输入用户名
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("hzxxfy6")
    # 输入密码
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("hxf124369")
    # 点击登录
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()
    print('登录成功')

# 判断是否登录
try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    print("未登录过！")
    login()
else:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    try:
        driver.find_element_by_xpath('//android.widget.TextView[@text="未登录"]')
    except NoSuchElementException:
        print("已登录！")
    else:
        driver.find_element_by_xpath('//android.widget.TextView[@text="未登录"]').click()
        print("未登录")
        login()