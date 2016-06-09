import unittest
from selenium import webdriver

class AweberTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('https://www.practiceselenium.com')
       
	#####################################
	#1 
    def menu(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Menu')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
	
	############################################
	#2 don't display line of organic tea
	def line_of_organic_teas(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('#wsb-element-00000000-0000-0000-0000-000450914876')
		search_link.send_keys('More')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
	
	###############################	
	#3 Don't show tea of the month club
	def tea_of_month_club(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('#wsb-element-00000000-0000-0000-0000-000450914877')
		search_link.send_keys('More')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
	
	##########################################33
	#4 Join Us text can't be clicked
	def join_us(self):
        self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Our Passion')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/our-passion.html"]'))
			
        join_link = self.driver.find_element_by_css_selector('')
		join_link.send_keys('Join Us')
        join_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/joinus.html"]'))
	
	##########################################################
	#5 Can not display Herbal Tea Collection
	def herbal_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Herbal Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/herbaltea.html"]'))
	
	###########################
	#6	Can not display Loose Tea Collection
	def loose_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Loose Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/loosetea.html"]'))
    
	#########################
	#7 Can not display Flavored Tea Collection
	def flavored_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Flavored Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/flavoredtea.html"]'))
	
	############################
	#8 Can not click Log In Text
	def login_page(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Menu')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/menu.html"]'))
		
		checkout_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		checkout_button.send_keys('Check Out')
        checkout_button.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/check-out.html"]'))
		
		login_text= self.driver.find_element_by_css_selector('#content input[type="text"]')
		login_text.send_keys('Log in')
        login_text.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/log-in.html"]'))
	
	#################
	#9 Can not continue to next step after click Place Order
	def checkout_process(self): 
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Menu')
        search_link.click()
		
		checkout_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		checkout_button.send_keys('Check Out')
        checkout_button.click()
		
		email = self.driver.find_element_by_id("email")
		name = self.driver.find_element_by_id("name")
		address = self.driver.find_element_by_id("address")

		email.send_keys("nama.kaka@yahoo.com")
		name.send_keys("nama")
		address.send_keys("Jalan Majapahit No. 13")
		
		card_type = self.driver.find_element_by_id("card_type")
		card_number = self.driver.find_element_by_id("card_number")
		cardholder_name = self.driver.find_element_by_id("cardholder_name")
		verification_code = self.driver.find_element_by_id("verification_code")
		
		card_type.send_keys("Visa")
		card_number.send_keys("8120122")
		cardholder_name.send_keys("Wiro")
		verification_code.send_keys("212")
		
		place_order_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		place_order_button.send_keys('Place Order')
        place_order_button.click()
	
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()<span style="font-size: 16px;"> </span>