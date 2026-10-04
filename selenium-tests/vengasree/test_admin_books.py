from common.conftest import login
from selenium.webdriver.common.by import By
import time

def test_admin_login_and_book_management(driver):
    login(driver)
    assert 'Dashboard' in driver.page_source
    driver.find_element(By.XPATH,'//button[contains(.,"Book Management")]').click()
    title=f'Selenium Book {int(time.time())}'
    inputs=driver.find_elements(By.CSS_SELECTOR,'.form-row input')
    values=[title,'Test Author',str(int(time.time())),'Testing','2']
    for el,val in zip(inputs[:5],values): el.send_keys(val)
    driver.find_element(By.XPATH,'//button[normalize-space()="Add"]').click()
    assert title in driver.page_source 
