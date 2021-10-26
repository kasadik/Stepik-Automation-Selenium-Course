from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
import unittest

class TestRegistration(unittest.TestCase):

    def test_registration2(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.first')
            input.send_keys('Hey')
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.second')
            input.send_keys('Hey')
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.third')
            input.send_keys('Hey')
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
            time.sleep(2)
            browser.quit()

    def test_registration1(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.first')
            input.send_keys('Hey')
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.second')
            input.send_keys('Hey')
            input=browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.third')
            input.send_keys('Hey')
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
            time.sleep(2)
            browser.quit()

if __name__=='__main__':
    unittest.main()