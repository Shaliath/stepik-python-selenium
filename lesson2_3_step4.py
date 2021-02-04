import time
import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	start_button = browser.find_element_by_css_selector("button.btn")
	start_button.click()

	confirm = browser.switch_to.alert
	confirm.accept()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	input_field = browser.find_element_by_id("answer")
	input_field.send_keys(y)

	submit = browser.find_element_by_css_selector("button.btn")
	submit.click()


finally:
	time.sleep(10)
	browser.quit()