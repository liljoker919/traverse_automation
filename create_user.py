from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://fieldservice919.herokuapp.com/")



driver.find_element_by_xpath("/html/body/section[1]/header/div/div/div[3]/a").click()





#driver.quit()
