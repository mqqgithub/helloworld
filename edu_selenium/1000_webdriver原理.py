# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;
from selenium import webdriver

driver = webdriver.Chrome()
print(type(driver))
print(driver)
driver.quit()
# <class 'selenium.webdriver.chrome.webdriver.WebDriver'> 返回类型WebDriver类
# <selenium.webdriver.chrome.webdriver.WebDriver (session="e433857c8408b51417446fbd0769881a")>
# 具体的对象就是加上session

'''
# driver = webdriver.Chrome()  webdriver是包名 Chrome()其实是chrome.webdriver模块中的WebDriver（）
# chromedriver.exe 文件放到环境变量 Path 所设置的目录下，如果前面我们已经将（C:\Python27 ）
# 添加到了环境变量 Path 所设置的目录，可以将 chromedriver.exe 放到 C:\Python27\目录下如果是jenkins执行，需要具体的路径
# jenkins使用这个方式避免采坑 java -jar "D:\Jenkins\jenkins.war"  --httpPort=9000   （服务器记得开放此端口，不然其他机器访问不到--坑）
# jenkins执行报错驱动放在和浏览器同一个文件及就可以了，但是不明白为什么，这个驱动放在其他地方就会报错
# driver = webdriver.Chrome("C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
'''
'''
webdriver  原理：
1. WebDriver 启动目标浏览器，并绑定到指定端口。该启动的浏览器实例，做为 web driver 的 remote server。
2. Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： thewebriver wire protocol）
3. Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe），来转
化转化浏览器的 native 调用。
https://www.cnblogs.com/augus007/articles/7338195.html
https://www.cnblogs.com/linbo3168/p/6704387.html
https://blog.csdn.net/u013434475/article/details/88415940
client（脚本webdriver API）---借助ComandExecutor转化为http请求---remote server（各种driver，native component组件转化为native invoke）---浏览器
'''