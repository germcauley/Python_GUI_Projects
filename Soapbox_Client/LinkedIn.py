from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
from hamcrest import *
import time

class LinkedIN(BasePage):


    def __init__(self):
        BasePage.__init__(
            self)

    #post on linkedin, take in user credentials,title of post,link/text, to post in
    def LI_post(self):

        LIhome = "https://www.linkedin.com/"
        email_field = "#login-email"
        pw_field = "#login-password"
        sign_in = "#login-submit"
        self.driver.navigate(LIhome)
        self.driver.find_elements_by_css_selector(email_field).sendkeys("asdasd")
        self.driver.find_elements_by_css_selector(pw_field).sendkeys("asdasd")
        self.driver.find_elements_by_css_selector(sign_in).click()

    def testmethod(self):
        print("asdsdsdasda")


