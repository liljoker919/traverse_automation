from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
import unittest
import time
import time
import random
import csv




class TestCase2(unittest.TestCase):

	def test_sign_up(self):
		driver = webdriver.Chrome()
		driver.implicitly_wait(10)
		driver.get("https://fieldservice919.herokuapp.com/")

		login_button = driver.find_element_by_xpath("/html/body/section[1]/header/div/div/div[3]/a")
		login_button.click()

		sign_up_button = driver.find_element_by_xpath("/html/body/div/section[1]/header/div/div/div[3]/a")
		sign_up_button.click()

		business_name_list = ["Cannon Aviation", "Solstice Brews", "Life Co.",  "Starecords",  "Squidustries","Hurricanetworks", "Crystalightning", "Angelhive", "Dragonfruit", "Ghostcloud", "Wave Industries","Sapling", "Ice"]
		business_name_random = random.choice(business_name_list)

		business_name_sign_up = driver.find_element_by_name("business[name]")
		business_name_sign_up.send_keys(business_name_random)

		street_list = ["1 Center Street", "2 8th Street West", "3 Oxford Court", "4 Lantern Lane", "5 Circle Drive", "6 Fieldstone Drive", "7 York Road", "8 State Street", "9 Hight Street", "10 Adams Avenue"]
		street_random = random.choice(street_list)


		street_address = driver.find_element_by_name("business[street]")
		street_address.send_keys(street_random)

		city_list = ["Arlington", "Aurora", "Bakersfield", "Cleveland", "Chandler", "Toledo", "Birmingam", "Haaleah", "North Hempstead", "Cheasapeake"]
		city_random = random.choice(city_list)

		city = driver.find_element_by_name("business[city]")
		city.send_keys(city_random)

		state_list = ["Indiana", "New Hampshire", "Tennessee", "Kanasas", "Iowa", "California", "Utah", "New Jersey", "Wisconsin", "Louisiana"]
		state_random = random.choice(state_list)

		state = driver.find_element_by_name("business[state]")
		state.send_keys(state_random)

		zipcode_random = random.randint(11111,99999)

		zipcode = driver.find_element_by_name("business[zip]")
		zipcode.send_keys(zipcode_random)

		phone_list = ("(935) 597-0748", "(384) 411-8931"  "(568) 283-0172", "(530) 403-4373", "(913) 645-1871", "(974) 921-6565", "(893) 678-8967", "(206) 526-4427","(556) 794-3520", "(750) 842-5637")
		phone_random = random.choice(phone_list)

		phone = driver.find_element_by_name("business[phone]")
		phone.send_keys(phone_random)

		next_button_sign_up = driver.find_element_by_xpath("/html/body/div/section[2]/div/div[2]/div[2]/div/form/div[7]/button")
		next_button_sign_up.click()

		first_name_signup_list = ["Clinton", "Charlene", "Simon", "Stuart", "Julia", "Jerome", "Catherine", "Herbert", "Shirley", "Gloria"]
		first_name_random = random.choice(first_name_signup_list)

		first_name_signup = driver.find_element_by_name("user[first_name]")
		first_name_signup.send_keys(first_name_random)

		last_name_signup_list = ["Copeland", "Frank", "Rogers" "Stone", "Ellis", "Christensen", "Luna", "Holloway", "Brown", "Hale"]
		last_name_signup_random = random.choice(last_name_signup_list)


		last_name_signup = driver.find_element_by_name("user[last_name]")
		last_name_signup.send_keys(last_name_signup_random)

		email_first = first_name_random.lower()
		email_last = last_name_signup_random.lower()
		new_user_email = (email_first.split()[0][0] + email_last + "@example.com")

		email = driver.find_element_by_name("user[email]")
		email.send_keys(new_user_email)

		register_password = driver.find_element_by_name("user[password]")
		register_password.send_keys("1traverse1")

		register_password_confirm = driver.find_element_by_name("user[confirm_password]")
		register_password_confirm.send_keys("1traverse1")

		register_button = driver.find_element_by_xpath("/html/body/div/section[2]/section/div/div[2]/div[2]/div/form/div[6]/button")
		register_button.click()

		url =  driver.current_url
		self.assertEqual(url, "https://fieldservice919.herokuapp.com/dashboards")

		new_user = first_name_random + " " + last_name_signup_random
		



		text_file = open("Output.txt", "a")
		text_file.write('\n' + "Name" + "          " + "Email"
						'\n' + new_user + "   " + new_user_email)
		text_file.close() 

		with open('new_user_signup.csv', 'a') as csvfile:
    			filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    			#filewriter.writerow(['Name', 'Email'])
    			filewriter.writerow([new_user, new_user_email])
    
 

 

		
 
print("writing complete")


if __name__ == '__main__':
	unittest.main(verbosity=2)