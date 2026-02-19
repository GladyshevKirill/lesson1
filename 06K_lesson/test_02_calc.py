# test_02_calc.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.ID, "delay").clear()
driver.find_element(By.ID, "delay").send_keys("45")

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

wait = WebDriverWait(driver, 50)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

result = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert result == "15"

driver.quit()