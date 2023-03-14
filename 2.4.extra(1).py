from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element(By.ID, "book")
button.click()

number = browser.find_element(By.ID, "input_value").text
number = calc(number)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(number)

button_2 = browser.find_element(By.ID, "solve")
button_2.click()



sleep(90)
browser.quit()
