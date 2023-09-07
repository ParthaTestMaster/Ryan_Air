import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def wait_until_element_is_clickable(self, locatortype, locatorvalue):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locatortype,locatorvalue)))
        return element

    def wait_until_element_is_visible(self,locatortype, locatorvalue):
        wait =WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locatortype,locatorvalue)))
        return element

    def scroll_using_offset(self):
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(5)

    def current_window_handle(self):
        current_window = self.driver.current_window_handle
        print('current window handle : ', current_window)

    def all_opened_window_handles(self):
        all_windows = self.driver.window_handles
        print("all window handles : ", all_windows)

    def switch_to_latest_window(self):
        ##get current window handle
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                time.sleep(5)
                break

