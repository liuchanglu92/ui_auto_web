from selenium import webdriver

def open_browser(name,url):
    if name == "chrome":
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver
class Testkeys(object):
    def __init__(self,name,url):
        self.driver = open_browser(name,url)
    def input_text(self,location,text):
        if location[0] == "xpath":
            self.driver.find_element_by_xpath(location[1]).send_keys(text)
        if location[0] =="id":
            self.driver.find_element_by_id(location[1]).send_keys(text)
        if location[0] == "name":
            self.driver.find_element_by_id(location[1]).send_keys(text)

    def click(self,location):
        if location[0] == "xpath":
            self.driver.find_element_by_xpath(location[1]).click()
        if location[0] =="id":
            self.driver.find_element_by_id(location[1]).click()
        if location[0] == "name":
            self.driver.find_element_by_id(location[1]).click()

    def get_url(self):
        current_url=self.driver.current_url()
        return current_url