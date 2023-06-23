import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://suninjuly.github.io/wait2.html')
    verify_button_locator = ('id', 'verify')
    wait = WebDriverWait(driver, timeout=5)
    verify_button = wait.until(EC.element_to_be_clickable(verify_button_locator))
    verify_button.click()
    verify_message = driver.find_element('id', 'verify_message')
    assert 'successful' in verify_message.text.lower()
finally:
    driver.quit()


try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    price_locator = ('id', 'price')
    book_button_locator = ('id', 'book')
    wait = WebDriverWait(driver, 15)
    price = wait.until(EC.text_to_be_present_in_element(price_locator, '100'))
    driver.find_element(*book_button_locator).click()
    x = int(driver.find_element('id', 'input_value').text)
    answer = math.log(abs(12 * math.sin(x)))
    driver.find_element('id', 'answer').send_keys(answer)
    submit_button_locator = ('css selector', '[type=submit]')
    driver.find_element(*submit_button_locator).click()
    time.sleep(3)
finally:
    driver.quit()
