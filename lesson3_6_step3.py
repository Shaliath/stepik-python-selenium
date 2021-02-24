import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_answer():
	return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_secret_message(browser, link):
	browser.get(link)
	text_box = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "textarea")))
	text_box.send_keys(str(get_answer()))

	button = browser.find_element_by_css_selector(".submit-submission")
	button.click()

	correct = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
	message = correct.text
	assert message == "Correct!", f"Expected 'Correct!', but was {message}"