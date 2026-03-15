import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(self.URL)

    def login_as(self, username: str, password: str) -> None:
        self.wait.until(
            ec.presence_of_element_located(self.USERNAME)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()


class InventoryPage:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_backpack(self) -> None:
        self.wait.until(
            ec.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

    def add_bolt_tshirt(self) -> None:
        self.wait.until(
            ec.element_to_be_clickable(self.ADD_BOLT_TSHIRT)
        ).click()

    def add_onesie(self) -> None:
        self.wait.until(
            ec.element_to_be_clickable(self.ADD_ONESIE)
        ).click()

    def go_to_cart(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.CART)).click()


class CartPage:
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def checkout(self) -> None:
        self.wait.until(
            ec.element_to_be_clickable(self.CHECKOUT)
        ).click()


class CheckoutInfoPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.wait.until(
            ec.presence_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self) -> None:
        self.wait.until(
            ec.element_to_be_clickable(self.CONTINUE)
        ).click()


class CheckoutOverviewPage:
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def total_value(self) -> str:
        total_text = self.wait.until(
            ec.presence_of_element_located(self.TOTAL)
        ).text
        return total_text.replace("Total: ", "").strip()


@allure.feature("Shop")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Магазин: итоговая сумма в checkout overview корректна")
@allure.description(
    "Добавляем 3 товара в корзину, оформляем заказ "
    "и проверяем итоговую сумму."
)
def test_shop_total() -> None:
    driver = webdriver.Firefox()
    try:
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        info = CheckoutInfoPage(driver)
        overview = CheckoutOverviewPage(driver)

        with allure.step("Открыть страницу логина"):
            login.open()

        with allure.step("Залогиниться standard_user / secret_sauce"):
            login.login_as("standard_user", "secret_sauce")

        with allure.step(
            "Добавить товары в корзину: backpack, bolt t-shirt, onesie"
        ):
            inventory.add_backpack()
            inventory.add_bolt_tshirt()
            inventory.add_onesie()

        with allure.step("Перейти в корзину"):
            inventory.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart.checkout()

        with allure.step("Заполнить данные покупателя"):
            info.fill(
                first_name="Ivan",
                last_name="Petrov",
                postal_code="123456",
            )

        with allure.step("Продолжить оформление заказа"):
            info.continue_checkout()

        with allure.step("Проверить итоговую сумму"):
            assert overview.total_value() == "$58.29"
    finally:
        driver.quit()