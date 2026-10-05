import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def app_page(page: Page):
    """
    Provides a Playwright Page object for each test.
    """

    page.goto("https://www.saucedemo.com/")

    yield page

    # Optional screenshot when test fails
    if not page.is_closed():
        page.close()
