import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def tes_1(self):
    url1 = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(url1)
    # Ваш код, который заполняет обязательные поля
    first = browser.find_element(By.CSS_SELECTOR, '[required].form-control.first')
    first.send_keys('Aboba')
    second = browser.find_element(By.CSS_SELECTOR, '[required].form-control.second')
    second.send_keys('Aboba2')
    third = browser.find_element(By.CSS_SELECTOR, '[required].form-control.third')
    third.send_keys('Aboba3')
    sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # Отправляем заполненную форму
    self.assertEquals("Congratulations! You have successfully registered!", welcome_text, "Something")


def test_2(self):
    url2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(url2)
    # Ваш код, который заполняет обязательные поля
    first = browser.find_element(By.CSS_SELECTOR, '[required].form-control.first')
    first.send_keys('Aboba')
    second = browser.find_element(By.CSS_SELECTOR, '[required].form-control.second')
    second.send_keys('Aboba2')
    third = browser.find_element(By.CSS_SELECTOR, '[required].form-control.third')
    third.send_keys('Aboba3')
    sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    self.assertEquals("Congratulations! You have successfully registered!", welcome_text, "Something")


if __name__ == "__main__":
    unittest.main()
