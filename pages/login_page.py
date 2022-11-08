from selenium import webdriver
from common.keys import Testkeys
from common.user import User
from location.login_locations import Login_locations
from time import sleep

class LoginPage():
    def login(self):
        self.driver = Testkeys('chrome','https://1.cih-index.com/sys/v2/kfyLogin')
        self.driver.click(Login_locations.account_Login)
        self.driver.input_text(Login_locations.user, User.username)
        self.driver.input_text(Login_locations.pwd,User.pwd)
        self.driver.click(Login_locations.btn_login)