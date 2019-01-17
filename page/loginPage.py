from selenium.webdriver.common.by import By
from common.change_open_browser import Browers


class LoginPage(Browers):


# userNameInput = By.CLASS_NAME("el-input el-input__inner")
# passWordInput = By.CLASS_NAME("el-input__inner")
# loginButton = By.CLASS_NAME("el-button el-button--default")
#
# userNameInput = By.CSS_SELECTOR("#app form div:first-child div .el-input input")
#
#
# def search(self):
#     print(self)

if __name__ == '__main__':
    login = LoginPage()
    # login.search()
