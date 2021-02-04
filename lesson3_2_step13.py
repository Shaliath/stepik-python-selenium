from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):

	def test_regiistration1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		first_name = browser.find_element_by_css_selector(".first:required")
		first_name.send_keys("First")
		last_name = browser.find_element_by_css_selector(".second:required")
		last_name.send_keys("Last")
		email = browser.find_element_by_css_selector(".third:required")
		email.send_keys("Email")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		expected = "Congratulations! You have successfully registered!"
		browser.quit()
		self.assertEqual(welcome_text, expected, f"Expected {expected}")

	def test_regiistration2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		first_name = browser.find_element_by_css_selector(".first:required")
		first_name.send_keys("First")
		last_name = browser.find_element_by_css_selector(".second:required")
		last_name.send_keys("Last")
		email = browser.find_element_by_css_selector(".third:required")
		email.send_keys("Email")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		expected = "Congratulations! You have successfully registered!"
		browser.quit()
		self.assertEqual(welcome_text, expected, f"Expected {expected}")

if __name__ == "__main__":
	unittest.main()