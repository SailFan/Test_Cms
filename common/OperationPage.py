import time
from selenium.webdriver.common.action_chains import ActionChains
from  common.change_open_browser import Browers

class OperationPage(Browers):
    def __init__(self, page = None, browser_type = "chrome"):
        if page:
            self.driver = page.driver
        else:
            super().__init__(browser_type=browser_type)
    # 获取当前窗口句柄
    @property
    def current_windows(self):
        return self.driver.current_window_handle

    #获取标题
    @property
    def get_title(self):
        return self.driver.title

    #获取当前地址
    def get_current_title(self):
        return self.driver.current_url

    def wait(self, seconds=3):
        time.sleep(seconds)

    def exectu(self, js, *args):
        self.driver.execute_script(js, *args)

    def move_to(self,to_element):
        ActionChains(self.driver).move_to_element(to_element).perform()

    def find_element(self,*args):
        return self.driver.find_element(*args)

    def find_elements(self,*args):
        return self.driver.find_elements(*args)
    def switch_to_windows(self,page_current_url, page_current_title ):
        all_windows = self.driver.window_handles
        if len(all_windows)==1:
            print("只有一个window")
        elif len(all_windows)==2:
            other_window = all_windows[1-all_windows.index(self.current_window)]
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





if __name__ == '__main__':
    operationPage = OperationPage("firefox")
    operationPage.get("https://www.baidu.com/")