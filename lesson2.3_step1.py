from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
# from numpy import sin


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
answer = browser.find_element(By.ID, 'answer').send_keys(y)

button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()


time.sleep(7)
browser.quit()
