from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://fieldservice919.herokuapp.com/")

class TestCase1(unittest.TestCase):

	def test_valid_login(self):
		driver = webdriver.Chrome()
		driver.implicitly_wait(10)
		driver.get("https://fieldservice919.herokuapp.com/")
		login_button = driver.find_element_by_xpath("/html/body/section[1]/header/div/div/div[3]/a")
		login_button.click()
		login_username = driver.find_element_by_name("user[email]")
		login_username.send_keys("jcollier@example.com")
		login_password = driver.find_element_by_name("user[password]")
		login_password.send_keys("1traverse1")
		submit_button = driver.find_element_by_xpath("/html/body/div/section[2]/div/div/div/div/form/button")
		submit_button.click()
		url =  driver.current_url
		self.assertEqual(url, "https://fieldservice919.herokuapp.com/customers")


	
if __name__ == '__main__':
	unittest.main(verbosity=2)