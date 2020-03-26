# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.set_window_size(1000, 800)
sleep(1)
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(5)
driver.back()
sleep(4)
driver.forward()
sleep(1)
driver.quit()


# driver.close()  只是关闭浏览器，但是进程还在
# driver.quit()  关闭进程

