from common.conftest import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_issue_and_return_flow(driver):
    login(driver)

    driver.find_element(
        By.XPATH,
        '//button[contains(.,"Issue / Return")]'
    ).click()

    wait = WebDriverWait(driver, 10)

    # Wait for books to load
    book_select = wait.until(
        lambda d: next(
            (
                s for s in d.find_elements(By.TAG_NAME, 'select')
                if len(s.find_elements(By.TAG_NAME, 'option')) > 1
            ),
            False
        )
    )

    # Select the first available book
    book_select.find_elements(
        By.TAG_NAME, 'option'
    )[1].click()

    # Wait for members to load
    member_select = wait.until(
        lambda d: next(
            (
                s for s in d.find_elements(By.TAG_NAME, 'select')
                if s != book_select
                and len(s.find_elements(By.TAG_NAME, 'option')) > 1
            ),
            False
        )
    )

    # Select a member that is not Selenium Member
    member_options = member_select.find_elements(
        By.TAG_NAME, 'option'
    )

    member_options[2].click()

    # Issue the book
    issue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[normalize-space()="Issue"]')
        )
    )
    issue_button.click()

    # Wait until an ISSUED transaction appears
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, 'body'),
            'ISSUED'
        )
    )

    # Return the issued book
    return_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[normalize-space()="Return"]')
        )
    )
    return_button.click()

    # Wait until RETURNED appears
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, 'body'),
            'RETURNED'
        )
    )