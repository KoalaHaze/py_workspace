# coding=utf-8
from kyb.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

# 输入错误用户名
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("hzxxfy6")
# 输入错误密码
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("dasw5aw48")
# 点击登录
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

exit_message = '账号不存在'
error_message = '用户名或密码错误，你还可以尝试4次'
limit_message = '验证失败次数过多，请15分钟后再试'

message='//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)
# message='//*[@text=\'{}\']'.format(exit_message)

toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)