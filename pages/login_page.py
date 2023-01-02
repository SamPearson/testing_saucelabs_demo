from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests import config


class LoginPage(BasePage):
    _login_wrapper = {"by": By.CLASS_NAME, "value": "login_wrapper"}
    _login_page_username_input = {"by": By.ID, "value": "user-name"}
    _login_page_password_input = {"by": By.ID, "value": "password"}
    _login_page_submit_button = {"by": By.ID, "value": "login-button"}

    _login_error = {"by": By.CLASS_NAME, "value": "error-message-container"}
    _invalid_login_error_message = "Epic sadface: Username and password do not match any user in this service"
    _locked_out_error_message = "Epic sadface: Sorry, this user has been locked out."

    # Logging in successfully directs the user to the inventory page, a locator is required
    # to confirm this was successful
    _inventory_container_locator = {"by": By.ID, "value": "inventory_container"}

    def access_login_page(self):
        self._visit(config.baseurl)
        assert self._find(self._login_wrapper)

    # TODO: Do not hardcode credentials here
    def attempt_login(self, username="standard_user", password="secret_sauce"):
        # Allows for failed login attempts without throwing exceptions
        # useful for testing error messages
        self._visit("/login")
        self._type(self._login_page_username_input, username)
        self._type(self._login_page_password_input, password)
        self._click(self._login_page_submit_button)

    def login(self, username="standard_user", password="secret_sauce"):
        self.attempt_login(username, password)
        assert not self._find(self._login_error), f"Login failed - " \
                                                  f"{self._find(self._login_error).text}"
        assert self._find(self._inventory_container_locator), "Login failed - " \
                                                              "Cannot locate inventory container"

    def login_error(self):
        if self._find(self._login_error):
            return self._find(self._login_error).text
        else:
            return False
