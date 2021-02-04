import time
import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	first_name = browser.find_element_by_name("firstname")
	first_name.send_keys("Name")

	last_name = browser.find_element_by_name("lastname")
	last_name.send_keys("Last name")

	email = browser.find_element_by_name("email")
	email.send_keys("email@email.com")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')

	file_input = browser.find_element_by_id("file")
	file_input.send_keys(file_path)

	submit = browser.find_element_by_css_selector("button.btn")
	submit.click()


finally:
	time.sleep(10)
	browser.quit()