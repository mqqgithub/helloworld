# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
title = driver.title
print(title)
c_url = driver.current_url
print(c_url)
driver.quit()