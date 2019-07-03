from kyb.capability import driver

# 输入错误用户名
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("hzxxfy6")
# 输入错误密码
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("dasw5aw48")

# 截图到当前文件夹
driver.save_screenshot('login.png')
# 保存截图到指定文件夹
driver.get_screenshot_as_file('E:\\save_imgs/login.png')

# 点击登录
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

