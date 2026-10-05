from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_member_management():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open the React application
        driver.get("http://localhost:5173")

        # Login as admin
        username = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Username']")
            )
        )
        password = driver.find_element(
            By.XPATH, "//input[@placeholder='Password']"
        )

        username.send_keys("admin")
        password.send_keys("Admin@123")

        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Login')]"
        ).click()

        # Open Members module
        members_link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Member Management')]")
            )
        )
        members_link.click()

        # Add a member
        member_username = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='username']")
            )
        )

        member_username.send_keys("selenium_member")

        driver.find_element(
            By.XPATH, "//input[@placeholder='first name']"
        ).send_keys("Selenium")

        driver.find_element(
            By.XPATH, "//input[@placeholder='last name']"
        ).send_keys("Member")

        driver.find_element(
            By.XPATH, "//input[@placeholder='phone']"
        ).send_keys("9876543210")

        driver.find_element(
            By.XPATH, "//input[@placeholder='address']"
        ).send_keys("Test Address")

        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Add')]"
        ).click()

        # Verify member appears
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Selenium Member')]")
            )
        )

        print("Mounika member management test passed")

    finally:
        driver.quit()
