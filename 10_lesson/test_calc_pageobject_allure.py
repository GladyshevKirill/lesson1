import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SlowCalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    DELAY = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver, timeout: int = 50) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        delay_input = self.wait.until(
            ec.presence_of_element_located(self.DELAY)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click(self, label: str) -> None:
        locator = (By.XPATH, f"//span[normalize-space()='{label}']")
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def wait_screen_text(self, text: str) -> None:
        self.wait.until(
            ec.text_to_be_present_in_element(self.SCREEN, text)
        )

    def screen_text(self) -> str:
        return self.wait.until(
            ec.presence_of_element_located(self.SCREEN)
        ).text


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Медленный калькулятор: 7 + 8 = 15")
@allure.description(
    "Проверка вычисления суммы на странице slow-calculator "
    "с установленной задержкой."
)
def test_slow_calculator() -> None:
    driver = webdriver.Chrome()
    try:
        page = SlowCalculatorPage(driver, timeout=50)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку вычисления 45 секунд"):
            page.set_delay(45)

        with allure.step("Ввести выражение 7 + 8 ="):
            page.click("7")
            page.click("+")
            page.click("8")
            page.click("=")

        with allure.step("Дождаться результата 15 на экране"):
            page.wait_screen_text("15")

        with allure.step("Проверить, что результат равен 15"):
            assert page.screen_text() == "15"
    finally:
        driver.quit()