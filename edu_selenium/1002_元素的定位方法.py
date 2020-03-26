# 元素定位的方法

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_name("wd").send_keys("python")
driver.find_element_by_tag_name("input").send_keys("python")
driver.find_element_by_class_name("s_ipt").send_keys("python")

# 超链接文本
driver.find_element_by_link_text("新闻").click()
driver.find_element_by_partial_link_text("新闻").click()

# xpath
driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
driver.find_element_by_xpath("//div[@id='u1']/a[0]").send_keys("1")
driver.find_element_by_xpath("//div[@id='hd' or @name=q']").send_keys("2")
driver.find_element_by_xpath("//input[contains(@id,'kw')]").send_keys("python")
# 用于知道超链接上显示的部分或全部文本信息
driver.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
# 用Text，直接查找页面当中所有的退出二字，经常用于纯文字的查找
driver.find_element_by_xpath('//*[text()="新闻"]').click()
# 当标签里面含有其他"<标签>+文字"时
driver.find_element_by_xpath("//*[contains(.,'新闻')]").click()

# css单一属性定位
# type selector
driver.find_element_by_css_selector("input")
# id
driver.find_element_by_css_selector("#kw")
# class
driver.find_element_by_css_selector(".s_ipt")
# 其他属性
driver.find_element_by_css_selector("[name='wd']")
driver.find_element_by_css_selector("[type='text']")

# 组合属性
# id组合属性
driver.find_element_by_css_selector("input#kw")
# class组合属性
driver.find_element_by_css_selector("input.s_ipt")
# 其他属性组合定位
driver.find_element_by_css_selector("input[name='wd']")
# 仅有属性名，没有属性值
driver.find_element_by_css_selector("input[name]")
# 2个属性组合定位
driver.find_element_by_css_selector("[name='wd'][autocomplete='off']")

# 模糊匹配属性值的方法
# <input type="submit" id="su" value="百度一下" class="bg s_btn">
# 属性值由多个空格隔开，匹配其中一个值的方法
driver.find_element_by_css_selector("input[class~='btn']")
# 匹配属性值为字符串开头的方法
driver.find_element_by_css_selector("input[class^='btn']")
# 匹配属性值字符串结尾的方法
driver.find_element_by_css_selector("input[class$='s_btn']")
# 匹配被-分割的属性值的方法,如上图的class
driver.find_element_by_css_selector("input[class|='bg']")  # 要求精确填写的属性值

# 层及定位
# E>F    E下面的F这个元素
driver.find_element_by_css_selector('from#form>span>input')  # id是form的form下面的span下面的input
# E:nth-child(n)  如上图,
driver.find_element_by_css_selector('#u1>a:nth-child(1)').click()  # id为u_sp的下面的第一个a标签。
# E:nth-last-child(n)，如字面意思：倒数第几个标签
driver.find_element_by_css_selector("#u1>a:nth-last-child(9)")
# 4：E:first-child,第一个标签
driver.find_element_by_css_selector("#u1>a:first-child")
# 5：E:last-child,最后一个标签
# 6：E:only-child,唯一的标签


# 元素操作的几个方法
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("1")
driver.find_element_by_id("su").click()
driver.find_element_by_id("su").submit()
# submit()要求提交对象是一个表单form标签，更强调对信息的提交。click()更强调事件的独立性。（比如，一个文字链接就不能用 submit()方法。）

# 通过By定位
# from selenium.webdriver.common.by import By
# find_element(By.ID,"kw")
# find_element(By.NAME,"wd")
# find_element(By.CLASS_NAME,"s_ipt")
# find_element(By.TAG_NAME,"input")
# find_element(By.LINK_TEXT,u"新闻")
# find_element(By.PARTIAL_LINK_TEXT,u"新")
# find_element(By.XPATH,"//*[@class='bg s_btn']")
# find_element(By.CSS_SELECTOR,"span.bg s_btn_wr>input#su")


# 获取属性
# 获得输入框的尺寸
# size=driver.find_element_by_id('kw').size

# 返回百度页面底部备案信息
# text=driver.find_element_by_id("cp").text

# 返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
# attribute=driver.find_element_by_id("kw").get_attribute('type')

# 返回元素的结果是否可见，返回结果为 True 或 False
# result=driver.find_element_by_id("kw").is_displayed()
