import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	input_field = browser.find_element_by_id("answer")
	input_field.send_keys(y)

	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()

	radio = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
	radio.click()


	submit = browser.find_element_by_css_selector("button.btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
	submit.click()


finally:
	time.sleep(10)
	browser.quit()