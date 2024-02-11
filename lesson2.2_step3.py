from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(value1, value2):
    rs = int(value1) + int(value2)
    return str(rs)


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    value2 = browser.find_element(By.XPATH, '//span[@id="num2"]').text

    result = calc(value1, value2)

    dropdown = browser.find_element(By.ID, "dropdown").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(result))

    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(str(result))


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
