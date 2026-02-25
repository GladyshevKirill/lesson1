from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator_result():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15"
    finally:
        driver.quit()