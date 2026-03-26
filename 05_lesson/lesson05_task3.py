from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

inp = driver.find_element(By.CSS_SELECTOR, "input")
inp.send_keys("Sky")
sleep(1)

inp.clear()
sleep(1)

inp.send_keys("Pro")
sleep(2)

driver.quit()
