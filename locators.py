from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    login_button =   driver.find_element_by_xpath("/html/body/section[1]/header/div/div/div[3]/a")
    login_username = driver.find_element_by_name("user[email]")
	#login_password = driver.find_element_by_name("user[password]")
	#submit_button = driver.find_element_by_xpath("/html/body/div/section[2]/div/div/div/div/form/button")
		


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass