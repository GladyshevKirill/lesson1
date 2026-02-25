from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

while True:
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    if len(images) >= 4 and all(img.get_attribute("src") for img in images[:4]):
        break

third_src = images[2].get_attribute("src")
print(third_src)

driver.quit()