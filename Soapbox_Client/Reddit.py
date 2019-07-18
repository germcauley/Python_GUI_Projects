from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePage import BasePage
from hamcrest import *
import time

class Reddit(BasePage):

    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, '#accept-cookie')

    def __init__(self):
        BasePage.__init__(
            self)

    #post on reddit, take in user credentials,title of post,link/text, subreddit to post in
    def reddit_post(self,credentials,title,link,text,sub):
        return 1