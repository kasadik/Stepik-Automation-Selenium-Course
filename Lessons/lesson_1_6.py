import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    text = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    browser.find_element(By.ID,'book').click()
    x=int(browser.find_element(By.ID,'input_value').text)
    solution=math.log(abs(12*math.sin(x)))
    browser.find_element(By.ID,'answer').send_keys(str(solution))
    browser.find_element(By.ID,'solve').click()
finally:
    time.sleep(5)
    browser.quit()