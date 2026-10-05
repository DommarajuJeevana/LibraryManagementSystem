import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options=Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    d=webdriver.Chrome(options=options)
    yield d
    d.quit()

def login(driver, username='admin', password='Admin@123'):
    driver.get('http://localhost:5173')
    driver.find_element('css selector','input[placeholder="Username"]').send_keys(username)
    driver.find_element('css selector','input[placeholder="Password"]').send_keys(password)
    driver.find_element('xpath','//button[normalize-space()="Login"]').click()
    return driver
