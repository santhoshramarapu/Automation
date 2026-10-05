
from playwright.sync_api import Page, expect

from pom.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.page.goto(self.URL)

    def enter_username(self, username: str):
        self.page.locator(self.USERNAME).fill(username)

    def enter_password(self, password: str):
        self.page.locator(self.PASSWORD).fill(password)

    def click_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_successful(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

    def verify_login_error(self):
        expect(
            self.page.locator(self.ERROR_MESSAGE)
        ).to_be_visible()

