import time
import os
from selenium import webdriver
from common.Path import DRIVERS_PATH,REPORT_PATH
DRIVERS_CHROME_PATH = os.path.join(DRIVERS_PATH,"chromedriver.exe")
DRIVERS_FIREFOX_PATH = os.path.join(DRIVERS_PATH,"IEDriverServer.exe")
DRIVERS_PHANTOMJS_PATH = os.path.join(DRIVERS_PATH,"phantomjs.exe")
TYPES = {"firefox": webdriver.Firefox, "chrome": webdriver.Chrome, "ie":webdriver.Ie, "phantomjs": webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': DRIVERS_FIREFOX_PATH, 'chrome': DRIVERS_CHROME_PATH, "phantomjs": DRIVERS_PHANTOMJS_PATH}

class UnSupportBrowserTypeError(Exception):
    pass


class Browers():
    def __init__(self, bowser_type = "firefox"):
        self._type = bowser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None
    #最大化屏幕， 跳转指定地址
    def get(self, url, maxmize_window = True, implicitly_wait=30):
        self.driver = self.browser(EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maxmize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self
    #截取屏幕
    def savaScreenShot(self,name="screenShot"):
        dayName = time.strftime("%Y%m%d", time.localtime(time.time()))
        screenshotPath = REPORT_PATH+'\screenshot_%s' %dayName
        if not os.path.exists(screenshotPath):
            os.makedirs(screenshotPath)
        tmImage = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        imagePath = screenshotPath+"\\"+tmImage+".png"
        print(imagePath)
        screenShot = self.driver.save_screenshot(imagePath)
        return  screenShot
    #关闭当前浏览器
    def close(self):
        self.driver.close()
    #退出当前浏览器
    def quit(self):
        self.driver.quit()
if __name__ == '__main__':
    b = Browers("chrome").get("http://www.baidu.com")
    b.savaScreenShot()
    b.quit()