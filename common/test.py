import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("D:\pycode\Test_Cms\drivers\chromedriver.exe")
driver.get("https://www.baidu.com/")
# driver.current_window_handle
# title = driver.title
# url = driver.current_url
# driver.execute()
# driver.execute_script()
# driver.window_handles
# driver.current_url
# driver.find_element_by_css_selector()
driver.find_element_by_id("kw").send_keys("python")
# driver.switch_to.frame()
# driver.switch_to.window(other_window)
# ActionChains(driver).move_to_element(to_element).perform()
# print(url)
# a = "http://www.baidu.com";
# b = "http://www.163.com"
# print(a is b)
# print(title)
time.sleep(3)
driver.quit()
# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')