from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 初始化浏览器对象
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
#browser = webdriver.Edge()
#browser = webdriver.PhantomJS()
#browser = webdriver.Safari()

#2 访问界面

url = "https://mail.163.com/"
browser.get(url)

# 3元素获取
# browser.find_element_by_id()#根据id获取
# browser.find_element_by_xpath()#根据xpath获取
# browser.find_elements_by_css_selector()#根据css选择器获取
# browser.find_element_by_class_name()#根据css获取
# browser.find_element_by_name()#根据name获取
# browser.find_element_by_link_text()#根据link精确定位
# browser.find_element_by_partial_link_text()#根据link模糊定位
# browser.find_element_by_tag_name()#根据tag_name定位元素

# 通用方法,需要传入两个参数， 查找方法和值， 结果与以上八种完全一致， 不过会用起来更灵活
# browser.find_element(By.xxx, "")
#
# 如果查找的元素在页面中是单个， 那么用以上方法就可以， 如果查找的元素有多个， 可以用browser.find_elements(),多了一个s, 如果还用browser.find_elements()查找
# 将只会得到第一个元素
print(browser.current_url)

userNameInput = browser.find_element(By.CSS_SELECTOR, ".u-input box input:first-child")
# passWordInput = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
# submitButton = browser.find_element(By.CSS_SELECTOR, "a[id='dologin']")
userNameInput.send_keys("m17600576201")
# passWordInput.send_keys("ww6201")
# submitButton.click()
