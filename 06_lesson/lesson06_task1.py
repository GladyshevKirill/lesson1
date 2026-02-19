from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://uitestingplayground.com/ajax")

wait = WebDriverWait(driver, 30)

wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton"))).click()

msg_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content p")))
print(msg_el.text)

driver.quit()