import logging
import unittest
from ddt import ddt,data,unpack
from dao.LoginDao import getUser
from page.loginPage import LoginPage
user = getUser()
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = LoginPage("chrome")
        cls.browser.get("http://test.admin.xxx.cn")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def setUp(self):
        self.browser.get("http://test.admin.xxx.cn")

    def tearDown(self):
        self.browser.delete_cookie()
        self.browser.refresh()
    # 登录流程
    def test(self):
        self.browser.inputPassword("vocy.cn")
        self.browser.inputUsername("admin")
        self.browser.loginButton()
        url = self.browser.get_current_url()
        # self.assertEqual(url, "http://test.admin.xxx.cn/#/home")
        self.assertEqual(self.browser.get_title, "欢迎页")
    @data(*user)
    @unpack
    def test_login(self, id, username, password, casename):
        logging.warning(id)
        self.browser.inputPassword(username)
        self.browser.inputUsername(password)
        logging.warning("测试用例标题")
        self.assertEqual(self.browser.get_title, "欢迎页")

if __name__ == '__main__':
    unittest.main()
