from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()

button_text = driver.find_element(By.ID, "updatingButton").text
print(button_text)

driver.quit()