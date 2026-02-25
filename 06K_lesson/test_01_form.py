from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation_colors():
    driver = webdriver.Edge()  
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        wait.until(EC.presence_of_element_located((By.NAME, "first-name"))).send_keys(
            "Иван"
        )
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # zip-code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()

        zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
        wait.until(lambda d: "alert-danger" in zip_code.get_attribute("class"))
        assert "alert-danger" in zip_code.get_attribute("class")

        green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]
        for field_id in green_fields:
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            wait.until(lambda d, el=field: "alert-success" in el.get_attribute("class"))
            assert "alert-success" in field.get_attribute("class")
    finally:
        driver.quit()
