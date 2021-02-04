import time
import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	start_button = browser.find_element_by_css_selector("button.trollface")
	start_button.click()

	new_tab = browser.window_handles[1]
	browser.switch_to.window(new_tab)

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