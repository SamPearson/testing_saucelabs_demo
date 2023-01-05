from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

from tests import config


class CustomerInfoPage(BasePage):
    _checkout_info_container = {"by": By.CLASS_NAME, "value": "checkout_info_container"}

    _first_name_input = {"by": By.ID, "value": "first-name"}
    _last_name_input = {"by": By.ID, "value": "last-name"}
    _postal_code_input = {"by": By.ID, "value": "postal-code"}

    _info_error_message = {"by": By.CLASS_NAME, "value": "error-message-container"}

    _checkout_button = {"by": By.ID, "value": "continue"}

    def fill_customer_info_form(self, first_name, last_name, zip_code):
        self._type(self._first_name_input, first_name)
        self._type(self._last_name_input, last_name)
        self._type(self._postal_code_input, zip_code)

    def error_message(self):
        error = self._find(self._info_error_message).text
        return error

    def proceed_to_checkout_confirmation(self):
        self._click(self._checkout_button)