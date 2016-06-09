import unittest
 
class PracticeSelenium(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
 
    def test_title(self):
        self.driver.get('https://www.practiceselenium.com')
        
	
	#1. show welcome menu
	
	def welcome(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Welcome')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/welcome.html"]'))
		
	#1.1 show herbal tea collection
	def herbal_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Herbal Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/herbaltea.html"]'))
		
	#1.2 show loose tea collection
	def loose_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Loose Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/loosetea.html"]'))
    
	#1.3 show flavored tea collection
	def flavored_tea_collections(self):
        self.driver.get('http://www.practiceselenium.com/welcome.html')
        editor_collections = self.driver.find_elements_by_css_selector('.editor_collections')
        tea_collection = [tea.text for tea in editor_collections]
        self.assertIn('Flavored Tea', tea_collection)
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.send_keys('See Collection')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.practiceselenium.com/flavoredtea.html"]'))
	
		
	#2. show our passion menu
	def our_passion(self):
        self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Our Passion')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/our-passion.html"]'))
			
        element = self.driver.find_elements_by_css_selector('#wsb-element-text')
        element_texts = [element.text for element in element]
        self.assertIn('Our Passion', element_texts)
        self.assertIn('The Experts', element_texts)
        
	#3. show tea menu
	def menu(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Menu')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
		
		tea_list = self.driver.find_elements_by_css_selector('#wsb-canvas-template-page')
        tea_texts = [tea.text for tea in tea_list]
        self.assertIn('Green Tea', tea_texts)
        self.assertIn('Red Tea', tea_texts)
		self.assertIn('Oolong Tea', tea_texts)
	
	#4. show lets talk tea menu	
	def lets_talk_tea(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Lets Talk Tea')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/let-s-talk-tea.html"]'))
		
		talk_tea_list = self.driver.find_elements_by_css_selector('#wsb-element')
        talk_tea_texts = [talk.text for talk in talk_tea_list]
        self.assertIn('map', talk_tea_texts)
        self.assertIn('Our Info', talk_tea_texts)
		self.assertIn('Send us an email', talk_tea_texts)
	
	#4.1 send email
	def send_email(self):
		self.driver.get('http://www.practiceselenium.com/let-s-talk-tea.html')
		search_input = self.driver.find_element_by_css_selector('#content input[type="text"]')
		search_input.send_keys('Name')
		search_input.send_keys('Email')
		search_input.send_keys('Subject')
		search_input.send_keys('Message')
		search_input.send_keys('Message')
		search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
		search_submit.click()
		
	#5. check out process
	def check_out(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('li>a')
		search_link.send_keys('Check Out')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/check-out.html"]'))
		
		
		proceed_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		proceed_button.send_keys('Proceed checkout')
        proceed_button.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/log-in.html"]'))
		
		
		username = self.driver.find_element_by_id("username")
		password = self.driver.find_element_by_id("password")
		
		login_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		login_button.send_keys('Log In')
        login_button.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/shipping.html"]'))
		
		shipping_courier = self.driver.find_element_by_id("shipping_courier")
		
		continue_button = self.driver.find_element_by_css_selector('#content input[type="button"]')
		continue_button.send_keys('Continue')
        continue_button.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/payment.html"]'))
		
		
		card_type = self.driver.find_element_by_id("card_type")
		card_number = self.driver.find_element_by_id("card_number")
		cardholder_name = self.driver.find_element_by_id("cardholder_name")
		verification_code = self.driver.find_element_by_id("verification_code")
		
		submit = self.driver.find_element_by_css_selector('#content input[type="button"]')
		submit.send_keys('Submit')
        submit.click()
		
	#6. show line organic tea
	def line_of_organic_teas(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('#wsb-element-00000000-0000-0000-0000-000450914876')
		search_link.send_keys('More')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
	
	#7. show tea of month club
	def tea_of_month_club(self):
		self.driver.get('https://practiceselenium.com')
		search_link = self.driver.find_element_by_css_selector('#wsb-element-00000000-0000-0000-0000-000450914877')
		search_link.send_keys('More')
        search_link.click()
		self.assertTrue(self.driver.find_element_by_css_selector('a[http://www.practiceselenium.com/menu.html"]'))
	
	
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()<span style="font-size: 16px;"> </span>
		