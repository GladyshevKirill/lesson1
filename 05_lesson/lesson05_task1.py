from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get("https://uitestingplayground.com/classattr")

button = driver.find_element(
    By.CSS_SELECTOR,
    "button.btn.class2.btn-primary.btn-test",
)
button.send_keys(Keys.ENTER)

sleep(10)
driver.quit()
