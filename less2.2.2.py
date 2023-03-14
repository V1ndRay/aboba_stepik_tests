import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, "firstname")
    first.send_keys('Имя')
    last = browser.find_element(By.NAME, "lastname")
    last.send_keys('Фамилия')
    email = browser.find_element(By.NAME, "email")
    email.send_keys('Почта@почта')
    file = browser.find_element(By.NAME, "file")
    directory_way = os.path.abspath(os.path.dirname(__file__))

    file.send_keys(os.path.join(directory_way, 'fio.txt'))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
