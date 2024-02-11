from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
book = browser.find_element(By.ID, 'book').click()

value = browser.find_element(By.ID, 'input_value')
value_text = value.text
result = calc(value_text)

field = browser.find_element(By.ID, 'answer')
field.send_keys(result)

button = browser.find_element(By.ID, 'solve').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
