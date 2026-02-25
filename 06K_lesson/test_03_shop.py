from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop_total_is_correct():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(
            "standard_user"
        )
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(
            "Ivan"
        )
        driver.find_element(By.ID, "last-name").send_keys("Petrov")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        total_text = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        total_value = total_text.replace("Total: ", "").strip()

        assert total_value == "$58.29"
    finally:
        driver.quit()
        