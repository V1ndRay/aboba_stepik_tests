import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.ID, "num1")
    value1 = value1.text
    value2 = browser.find_element(By.ID, "num2")
    value2 = value2.text

    selector = Select(browser.find_element(By.TAG_NAME, "select"))
    selector.select_by_visible_text(str(int(value1)+int(value2)))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла