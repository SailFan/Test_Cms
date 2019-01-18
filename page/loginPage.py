from selenium.webdriver.common.by import By
from common.change_open_browser import Browers
import logging
from selenium.webdriver.common.keys import Keys


class LoginPage(Browers):
    userNameInput = (By.CSS_SELECTOR, "input[type='text']")
    passWordInput = (By.CSS_SELECTOR, "input[type='password']")
    login_button = (By.CSS_SELECTOR, ".el-button el-button--primary")
    reset_button = (By.CSS_SELECTOR, ".el-button el-button--default")
    kw_input = (By.CSS_SELECTOR, "#kw")
    def inputUsername(self, username):
        input_username = self.find_element(*self.userNameInput)
        if input_username is not None:
            input_username.clear()
            input_username.send_keys(username)
        else:
            logging.debug("没有找到用户名输入框")
    def inputPassword(self, password):
        self.find_element(*self.passWordInput).clear()
        self.find_element(*self.passWordInput).send_keys(password)

    def loginButton(self):
        self.find_element(*self.login_button).click()

    def resetButton(self):
        self.find_element(*self.reset_button).click()

    def kw(self, kwValue):
        self.find_element(*self.kw_input)

if __name__ == '__main__':
    pass
    # loginPage = LoginPage("chrome");
    # loginPage.get("http://test.admin.vocy.cn/#/login")
    # loginPage.inputUsername("dfff")
    # loginPage.quit()
