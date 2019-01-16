
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("D:\pycode\Test_Cms\drivers\chromedriver.exe")
driver.get("https://www.baidu.com/")
driver.current_window_handle
title = driver.title
url = driver.current_url
driver.execute()
driver.execute_script()
driver.window_handles
driver.current_url
driver.switch_to.frame()
driver.switch_to.window(other_window)
ActionChains(driver).move_to_element(to_element).perform()
print(url)
a = "http://www.baidu.com";
b = "http://www.163.com"
print(a is b)
print(title)
driver.quit()