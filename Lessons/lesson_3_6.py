import time
from selenium.webdriver.common.by import By
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)
    text=browser.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert  "Ajouter au panier"==text