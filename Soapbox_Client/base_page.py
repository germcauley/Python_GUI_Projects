from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 30

    def navigate(self, address):
        self.driver.get(address)