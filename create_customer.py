from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time
import random





class TestCase2(unittest.TestCase):

	def test_create_customer(self):
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
		driver.get("https://fieldservice919.herokuapp.com/customers/new")

		customer_name_list = ["Marcus Mcdonald", "Shannon Murray", "Judith Banks", "Willie James", "Rachael Mcdaniel","Denise Fox", "Robin Hicks", "Carl Harrington", "Ismeal Gutierrez", "Clinton King"]
		customer_name_random = random.choice(customer_name_list)

		customer_name = driver.find_element_by_name("customer[name]")
		customer_name.send_keys(customer_name_random)

		street_list = ["1 Center Street", "2 8th Street West", "3 Oxford Court", "4 Lantern Lane", "5 Circle Drive", "6 Fieldstone Drive", "7 York Road", "8 State Street", "9 Hight Street", "10 Adams Avenue"]
		street_random = random.choice(street_list)


		street_address = driver.find_element_by_name("customer[street]")
		street_address.send_keys(street_random)

		city_list = ["Arlington", "Aurora", "Bakersfield", "Cleveland", "Chandler", "Toledo", "Birmingam", "Haaleah", "North Hempstead", "Cheasapeake"]
		city_random = random.choice(city_list)

		city = driver.find_element_by_name("customer[city]")
		city.send_keys(city_random)

		state_list = ["Indiana", "New Hampshire", "Tennessee", "Kanasas", "Iowa", "California", "Utah", "New Jersey", "Wisconsin", "Louisiana"]
		state_random = random.choice(state_list)

		state = driver.find_element_by_name("customer[state]")
		state.send_keys(state_random)

		zipcode_random = random.randint(11111,99999)

		zipcode = driver.find_element_by_name("customer[zip]")
		zipcode.send_keys(zipcode_random)

		phone_list = ("(935) 597-0748", "(384) 411-8931"  "(568) 283-0172", "(530) 403-4373", "(913) 645-1871", "(974) 921-6565", "(893) 678-8967", "(206) 526-4427","(556) 794-3520", "(750) 842-5637")
		phone_random = random.choice(phone_list)

		phone = driver.find_element_by_name("customer[phone]")
		phone.send_keys(phone_random)

		email_remove_space = customer_name_random.lower().replace(" ", ".")

		email = driver.find_element_by_name("customer[email]")
		email.send_keys(email_remove_space + "@example.com")

		create_button = driver.find_element_by_xpath("/html/body/section/div/div/form/div[8]/input")
		create_button.click()

		confirm_created_created_customer = driver.find_element_by_id("noemail_remove_spacetice").text


		self.assertEqual(confirm_created_created_customer, "Customer was successfully created.")

		with open('new_user_signup.csv', 'a') as csvfile:
    			filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    			filewriter.writerow(['Name', 'Email'])
    			filewriter.writerow([customer_name_random, email_remove_space])
    



	
		

if __name__ == '__main__':
	unittest.main(verbosity=2)