from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text

y = calc(x)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)

button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()


alert = browser.switch_to.alert

alert_text = alert.text
print(alert_text)
time.sleep(5)

browser.quit()
