from selenium.webdriver.common.by import By
from common.change_open_browser import Browers
from selenium.common.exceptions import NoSuchElementException
import logging
import time


class LoginPage(Browers):
    userNameInput = (By.CSS_SELECTOR, "input[type='text']")
    passWordInput = (By.CSS_SELECTOR, "input[type='password']")
    login_button = (By.CSS_SELECTOR, "button:first-child")
    reset_button = (By.CSS_SELECTOR, "button:nth-child(2)")
    kw_input = (By.CSS_SELECTOR, "#kw")
    def inputUsername(self, username):
        try:
            input_username = self.find_element(*self.userNameInput)
            input_username.clear()
            input_username.send_keys(username)
        except NoSuchElementException as msg:
            logging.debug(u"查找元素异常%s"%msg)
            logging.debug("llllllllllllllllllllllllll")
    def inputPassword(self, password):
        try:
            input_password =self.find_element(*self.passWordInput)
            input_password.clear()
            input_password.send_keys(password)
        except NoSuchElementException as msg:
            logging.debug(u"查找元素异常%s" % msg)

    def loginButton(self):
        try:
            login_bnutton = self.find_element(*self.login_button)
            login_bnutton.click()
        except NoSuchElementException as msg:
            print(u"查找元素异常%s" % msg)


    def resetButton(self):
        try:
            resetButton = self.find_element(*self.reset_button)
            resetButton.click()
        except NoSuchElementException as msg:
            print(u"查找元素异常%s" % msg)

    def kw(self, kwValue):
        try:
            s_input = self.find_element(*self.kw_input)
            s_input.clear()
            s_input.send_keys(kwValue)
        except NoSuchElementException:
            logging.debug("没有找到搜索框元素")
if __name__ == '__main__':
    loginPage = LoginPage("chrome");
    loginPage.get("http://test.admin.xxx.cn/#/login")
    loginPage.inputUsername("admin")
    loginPage.inputPassword("111111")
#    loginPage.loginButton()
    loginPage.resetButton()
    time.sleep(3)
