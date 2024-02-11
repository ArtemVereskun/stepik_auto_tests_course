from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element(By.NAME, 'firstname')
firstname.send_keys("Artem")

lastname = browser.find_element(By.NAME, 'lastname')
lastname.send_keys("Ver")

email = browser.find_element(By.NAME, 'email')
email.send_keys("qwerty@gmail.com")


# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'file.txt')


file = browser.find_element(By.NAME, 'file')

# file.send_keys(file_path)
file.send_keys('C:\\file.txt')

button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()


time.sleep(10)
browser.quit()
