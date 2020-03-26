# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
size = driver.find_element_by_xpath("//input[@id='kw']").size
print(size)
name = driver.find_element_by_xpath("//*[contains(@id,'kw')]").get_attribute("class")
print(name)
display = driver.find_element_by_xpath("//*[contains(text(),'抗击肺炎')]").is_displayed()
print(display)
driver.quit()