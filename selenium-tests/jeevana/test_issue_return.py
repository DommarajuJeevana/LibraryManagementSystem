from common.conftest import login
from selenium.webdriver.common.by import By

def test_issue_and_return_flow(driver):
    login(driver)
    driver.find_element(By.XPATH,'//button[contains(.,"Issue / Return")]').click()
    selects=driver.find_elements(By.TAG_NAME,'select')
    selects[0].find_elements(By.TAG_NAME,'option')[1].click()
    selects[1].find_elements(By.TAG_NAME,'option')[1].click()
    driver.find_element(By.XPATH,'//button[normalize-space()="Issue"]').click()
    assert 'Issued' in driver.page_source
    return_buttons=driver.find_elements(By.XPATH,'//button[normalize-space()="Return"]')
    assert return_buttons
    return_buttons[0].click()
    assert 'Returned' in driver.page_source
