import time
import os
from selenium import webdriver
from common.Path import DRIVERS_PATH, REPORT_PATH
from selenium.webdriver.common.action_chains import ActionChains

DRIVERS_CHROME_PATH = os.path.join(DRIVERS_PATH, "chromedriver.exe")
DRIVERS_FIREFOX_PATH = os.path.join(DRIVERS_PATH, "IEDriverServer.exe")
DRIVERS_PHANTOMJS_PATH = os.path.join(DRIVERS_PATH, "phantomjs.exe")
TYPES = {"firefox": webdriver.Firefox, "chrome": webdriver.Chrome, "ie": webdriver.Ie, "phantomjs": webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': DRIVERS_FIREFOX_PATH, 'chrome': DRIVERS_CHROME_PATH, "phantomjs": DRIVERS_PHANTOMJS_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browers():
    def __init__(self, bowser_type):
        self._type = bowser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    # 最大化屏幕， 跳转指定地址
    def get(self, url, maxmize_window=True, implicitly_wait=30):
        self.driver = self.browser(EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maxmize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    # 截取屏幕
    def savaScreenShot(self, name="screenShot"):
        dayName = time.strftime("%Y%m%d", time.localtime(time.time()))
        screenshotPath = REPORT_PATH + '\screenshot_%s' % dayName
        if not os.path.exists(screenshotPath):
            os.makedirs(screenshotPath)
        tmImage = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        imagePath = screenshotPath + "\\" + tmImage + ".png"
        print(imagePath)
        screenShot = self.driver.save_screenshot(imagePath)
        return screenShot

    @property
    def current_windows(self):
        return self.driver.current_window_handle

    # 获取标题
    @property
    def get_title(self):
        return self.driver.title

    # 获取当前地址
    def get_current_title(self):
        return self.driver.current_url

    def exectu(self, js, *args):
        self.driver.execute_script(js, *args)

    def wait(self, seconds=3):
        time.sleep(seconds)

    def move_to(self, to_element):
        ActionChains(self.driver).move_to_element(to_element).perform()

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def switch_to_windows(self, page_current_url, page_current_title):
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            print("只有一个window")
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if page_current_url == self.driver.current_url or page_current_title == self.driver.title:
                    break
        print("logging")

    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def select_to(self):

        def close(self):
            self.driver.close()

    # 退出当前浏览器
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    b = Browers("chrome").get("http://www.baidu.com")
    b.savaScreenShot()
    print(b.get_title)
    b.quit()
