
from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value: str):
        self.page.locator(locator).fill(value)

