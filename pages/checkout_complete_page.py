from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutConfirmPage(BasePage):
    _checkout_complete_container = {"by": By.ID, "value": "checkout_complete_container"}

    _return_to_products_button = {"by": By.ID, "value": "back-to-products"}

    def checkout_complete(self):
        return bool(self._find(self._checkout_complete_container))

    def return_to_store(self):
        self._click(self._return_to_products_button)