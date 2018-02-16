
from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time

def setUp(self):
		global driver
		driver = webdriver.Chrome()
		driver.implicitly_wait(10)
		driver.get("https://fieldservice919.herokuapp.com/")


def tearDown(self):
		driver.quit()


