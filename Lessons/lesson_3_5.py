import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    time.sleep(1)
    browser.quit()

list_of_links=[
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]
@pytest.mark.parametrize('link', list_of_links)
def test_stepik(browser, link):
    link = link
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR,'.quiz-component.ember-view textarea').send_keys(answer)
    browser.find_element(By.CLASS_NAME,'submit-submission').click()
    correct = browser.find_element(By.CLASS_NAME,'smart-hints__hint').text
    assert correct=='Correct!'

