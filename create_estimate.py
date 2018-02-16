from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.ui            import Select 
import unittest
import time
import random






class TestCase2(unittest.TestCase):

	def test_create_estimate(self):
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
		
		estimate_button = driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[2]/a")
		estimate_button.click()

		add_new_estimate_button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/span[2]/a")
		add_new_estimate_button.click()

		customer_list_estimate = ["Ira Hernandez", "Vivian Davis", "Travis Fowler", "Gwen Gibson", "Judith Matis"
								  "Jeannette Lowe", "Robin Hicks", "Rachael Mcdaniel", "John", "Clinton King", "Denise Fox" ]

		random_customer = random.choice(customer_list_estimate)

		customer_name = driver.find_element_by_id("estimate_customer_id")
		Select(customer_name).select_by_visible_text(random_customer)

		service_name = driver.find_element_by_id("estimate_line_items_attributes_0_name")
		service_name.send_keys("A service that will be provided")

		description = driver.find_element_by_id("estimate_line_items_attributes_0_description")
		description.send_keys("A description of the service that will be provided")

		unit_price = driver.find_element_by_id("estimate_line_items_attributes_0_unit_price")
		unit_price.send_keys("250.00")

		quantity = driver.find_element_by_id("estimate_line_items_attributes_0_quantity")
		quantity.send_keys("25")

		delivery_date = driver.find_element_by_id("estimate_delivery_time")
		delivery_date.send_keys("10102019")

		create_estimate_button = driver.find_element_by_xpath("/html/body/section/div/div/div[3]/form/div[6]/input")
		create_estimate_button.click()




if __name__ == '__main__':
	unittest.main(verbosity=2)