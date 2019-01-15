import time
import os
from selenium import webdriver
from common.Path import DRIVERS_PATH
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