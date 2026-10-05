from pom.login_page import LoginPage


def test_valid_login(app_page):

    login_page = LoginPage(app_page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    login_page.verify_login_successful()