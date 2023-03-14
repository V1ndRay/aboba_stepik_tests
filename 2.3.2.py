from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.TAG_NAME, "button")
    first.click()
    window = browser.window_handles[1]
    browser.switch_to.window(window)
    number = browser.find_element(By.ID, "input_value").text
    number = calc(number)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(number)
    button_2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_2.click()

finally:
    sleep(20)
    browser.quit()
