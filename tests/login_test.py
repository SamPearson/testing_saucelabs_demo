import pytest
from pages.login_page import LoginPage


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self, driver):
        page = LoginPage(driver)
        page.access_login_page()
        return page

    def test_valid_credentials(self, login_page):
        login_page.login()

    def test_invalid_credentials(self, login_page):
        login_page.attempt_login(username="invalid_username", password="invalid_password")
        error = login_page.login_error()
        assert error, "Attempted to log in with invalid credentials," \
                                         " could not find error message."

        assert error == login_page._invalid_login_error_message, \
            f"Unexpected error message '{error}'. " \
            f"Expected '{login_page.login_page._invalid_login_error_message}'."

    def test_locked_out_user(self, login_page):
        login_page.attempt_login(username="locked_out_user", password="secret_sauce")
        error = login_page.login_error()
        assert error, "Attempted to log in with locked out user," \
                      " could not find error message."

        assert error == login_page._locked_out_error_message, \
            f"Unexpected error message '{error}'. " \
            f"Expected '{login_page.login_page._locked_out_error_message}'."
