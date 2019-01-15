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
    def get(self, url, maxmize_window = True, implicitly_wait=30):
        self.driver = self.browser(EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maxmize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self
    def savaScreenShot(self,name="screenShot"):
        dayName = time.strftime("%Y%m%d", time.localtime(time.time()))
        print(dayName)
        screenshotPath = REPORT_PATH+'\screenshot_%s' %dayName
        print(screenshotPath+"-------------------------------------")
        print(REPORT_PATH+"----------------------------------")
        if not os.path.exists(screenshotPath):
            os.makedirs(screenshotPath)
        tmImage = time.strftime("%H%M%S", time.localtime(time.time()))
        screenShot = self.driver.save_screenshot(screenshotPath.join(name).join(tmImage))
        return  screenShot
    def close(self):
        self.driver.close()
 r 
    def quit(self):
        self.driver.quit()
if __name__ == '__main__':
    b = Browers("chrome").get("http://www.baidu.com")
    b.savaScreenShot("lww")
    b.quit()