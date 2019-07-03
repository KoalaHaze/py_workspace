from kyb.capability import driver,NoSuchElementException
import random

driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()

images=driver.find_elements_by_id("com.tal.kaoyan:id/iv_picture")
images[5].click()

driver.find_element_by_id("com.tal.kaoyan:id/picture_tv_ok").click()
driver.find_element_by_id("com.tal.kaoyan:id/menu_crop").click()

username='zfxx'+str(random.randint(1000,9000))
print('用户名：',username)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext").send_keys(username)

password='htzq'+str(random.randint(1000,9999))
print('密码：',password)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext").send_keys(password)

email='zfkj'+str(random.randint(10000,90000))+'@163.com'
print('邮箱：',email)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext").send_keys(email)

driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn").click()


# 专业选择
driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major").click()

driver.find_elements_by_id("com.tal.kaoyan:id/major_subject_title")[1].click()
driver.find_elements_by_id("com.tal.kaoyan:id/major_group_title")[0].click()
driver.find_elements_by_id("com.tal.kaoyan:id/major_search_item_name")[1].click()

# 选择学校
driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_school").click()
#
# 定位不到添加院校按钮
# driver.find_element_by_xpath("//android.widget.LinearLayout[@text='添加院校']").click()

driver.find_elements_by_id("com.tal.kaoyan:id/more_forum_title")[1].click()
driver.find_elements_by_id("com.tal.kaoyan:id/university_search_item_name")[1].click()

driver.find_element_by_xpath("//android.widget.LinearLayout[@text='确定']").click()

# 进入考研帮
driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_goBtn").click()
