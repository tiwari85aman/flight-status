from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os, json
from bs4 import BeautifulSoup


class WebController(object):
    def __init__(self):
        self.driver = self.setup()
        self.max_delay_timeout = 25

    def setup(self):
        # instantiate a chrome options object so you can set the size and headless preference
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd() + "/chromedriver"
        return webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, tag_type, name):
        element = None
        if tag_type == "id":
            element = self.driver.find_element_by_id(name)
        elif tag_type == "class":
            element = self.driver.find_element_by_class_name(name)
        return element

    def input_text(self, tag_type, name, value):
        input_element = self.get_element(tag_type, name)
        input_element.send_keys(value)

    def click_element(self, tag_type, name):
        element = self.get_element(tag_type, name)
        self.driver.execute_script("arguments[0].click();", element)

    def get_attribute(self, tag_type, name, attribute):
        element = self.get_element(tag_type, name)
        return element.get_attribute(attribute)

    def wait_till_load(self, tag_type, name):
        BY = {
            "class": By.CLASS_NAME,
            "id": By.ID
        }
        try:
            WebDriverWait(self.driver, self.max_delay_timeout).until(
                EC.presence_of_element_located((BY[tag_type], name)))
            return True

        except TimeoutException:
            print("Loading took too much time!")
            return False

    def exit_driver(self):
        self.driver.quit()
