from common.conftest import login
from selenium.webdriver.common.by import By

def test_search_and_book_availability(driver):
    login(driver)
    driver.find_element(By.XPATH,'//button[contains(.,"Search & Availability")]').click()
    search=driver.find_element(By.CSS_SELECTOR,'.form-row input')
    search.send_keys('Clean Code')
    driver.find_element(By.XPATH,'//button[normalize-space()="Search"]').click()
    assert 'Clean Code' in driver.page_source
    assert 'Available' in driver.page_source or 'Not Available' in driver.page_source
