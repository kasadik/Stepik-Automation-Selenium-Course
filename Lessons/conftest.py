import pytest
from selenium import webdriver
import time
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    time.sleep(1)
    browser.quit()