from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://www.unillanos.edu.co/")
		self.assertIn("Universidad de los Llanos", browser.title)
	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()