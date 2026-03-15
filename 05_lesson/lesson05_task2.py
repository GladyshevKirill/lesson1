from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
driver.get("https://uitestingplayground.com/dynamicid")

d_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
d_button.click()

sleep(10)
driver.quit()
