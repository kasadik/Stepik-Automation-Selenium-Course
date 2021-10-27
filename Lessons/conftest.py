import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name=request.config.getoption('browser_name')
    if browser_name=='chrome':
        browser=webdriver.Chrome()
        browser.implicitly_wait(3)
        yield browser
        browser.quit()
    if browser_name=='firefox':
        browser=webdriver.Firefox()
        browser.implicitly_wait(3)
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    time.sleep(1)
    browser.quit()