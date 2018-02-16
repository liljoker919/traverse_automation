from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.ui            import Select 
import unittest
import time
import random






class TestCase2(unittest.TestCase):

	def test_create_invoice(self):
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

		invoice_button = driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[4]/a")
		invoice_button.click()

		add_new_invoice_button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/span[2]/a")
		add_new_invoice_button.click()

		customer_list_invoice = ["Ira Hernandez", "Vivian Davis", "Travis Fowler", "Gwen Gibson", "Judith Matis"
								  "Jeannette Lowe", "Robin Hicks", "Rachael Mcdaniel", "John", "Clinton King", "Denise Fox" ]

		random_customer = random.choice(customer_list_invoice)

		customer_name = driver.find_element_by_id("invoice_customer_id")
		Select(customer_name).select_by_visible_text(random_customer)

		service_name = driver.find_element_by_id("invoice_line_items_attributes_0_name")
		service_name.send_keys("A service that will be provided")

		description = driver.find_element_by_id("invoice_line_items_attributes_0_description")
		description.send_keys("A description of the service that will be provided")

		unit_price_random = random.randint(1,999)
		unit_price = driver.find_element_by_id("invoice_line_items_attributes_0_unit_price")
		unit_price.send_keys(unit_price_random)

		quantity_random = random.randint(1,99)
		quantity = driver.find_element_by_id("invoice_line_items_attributes_0_quantity")
		quantity.send_keys(quantity_random)

		invoice_date = driver.find_element_by_id("invoice_date")
		invoice_date.send_keys("10102019")

		invoice_due_date = driver.find_element_by_id("invoice_due_date")
		invoice_due_date.send_keys("10102019")

		create_invoice_button = driver.find_element_by_xpath("/html/body/section/div/div/div[3]/form/div[6]/input")
		create_invoice_button.click()




if __name__ == '__main__':
	unittest.main(verbosity=2)