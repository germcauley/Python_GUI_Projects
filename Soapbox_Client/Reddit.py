from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
from hamcrest import *
import time

class Reddit(BasePage):

    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, '#accept-cookie')

    name = "TheIrishRight"
    pw = "Jb97@tw0xrrZ"
    reddithome = "https://old.reddit.com/"

    def __init__(self):
        BasePage.__init__(
            self)

    #post on reddit, take in user credentials,title of post,link/text, subreddit to post in
    def reddit_post(self):
        name = "TheIrishRight"
        pw = "Jb97@tw0xrrZ"
        reddithome = "https://old.reddit.com/"
        self.driver.navigate(self,reddithome)