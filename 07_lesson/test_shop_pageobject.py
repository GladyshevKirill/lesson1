from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(self.URL)

    def login_as(self, username: str, password: str) -> None:
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys(
            username
        )
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()


class InventoryPage:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_backpack(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.ADD_BACKPACK)).click()

    def add_bolt_tshirt(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.ADD_BOLT_TSHIRT)).click()

    def add_onesie(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.ADD_ONESIE)).click()

    def go_to_cart(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.CART)).click()


class CartPage:
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def checkout(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.CHECKOUT)).click()


class CheckoutInfoPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.wait.until(ec.presence_of_element_located(self.FIRST_NAME)).send_keys(
            first_name
        )
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.CONTINUE)).click()


class CheckoutOverviewPage:
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def total_value(self) -> str:
        total_text = self.wait.until(ec.presence_of_element_located(self.TOTAL)).text
        return total_text.replace("Total: ", "").strip()


def test_shop_total():
    driver = webdriver.Firefox()

    try:
        login = LoginPage(driver)
        login.open()
        login.login_as("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_bolt_tshirt()
        inventory.add_onesie()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        info = CheckoutInfoPage(driver)
        info.fill(first_name="Ivan", last_name="Petrov", postal_code="123456")
        info.continue_checkout()

        overview = CheckoutOverviewPage(driver)
        assert overview.total_value() == "$58.29"
    finally:
        driver.quit()
        