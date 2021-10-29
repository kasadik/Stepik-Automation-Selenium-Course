import time
from selenium.webdriver.common.by import By
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(3)
    button=browser.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert  button