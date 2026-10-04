from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dashboard_and_reports():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://localhost:5173")

        # Login
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

        # Dashboard
        dashboard = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Dashboard')]")
            )
        )
        dashboard.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Total Books')]")
            )
        )

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Total Copies')]")
            )
        )

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Available Copies')]")
            )
        )

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Total Members')]")
            )
        )

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Active Issues')]")
            )
        )

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Returned Books')]")
            )
        )

        # Reports
        reports = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Transactions / Reports')]")
            )
        )
        reports.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Transactions / Reports')]")
            )
        )

        print("Madhupriya dashboard and reports test passed")

    finally:
        driver.quit()