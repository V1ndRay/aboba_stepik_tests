import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(10)
button = browser.find_element(By.ID, "submit_button")
button.click()
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()