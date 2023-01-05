from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

from tests import config


class CartPage(BasePage):
    _cart_contents_container = {"by": By.ID, "value": "cart_contents_container"}

    _cart_item = {"by": By.CLASS_NAME, "value": "cart_item"}
    _item_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _item_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _item_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _remove_button = {"by": By.CLASS_NAME, "value": "cart_button"}

    _checkout_button = {"by": By.ID, "value": "checkout"}

    def access_cart_page(self):
        login_page = LoginPage(self.driver)
        login_page.access_login_page()
        login_page.login()
        self._visit("/cart.html")
        assert self._find(self._cart_contents_container)

    def cart_items(self):
        items = []
        item_elements = self._find_all(self._cart_item)
        for i in item_elements:
            items.append({
                "name": self._find_child(i, self._item_name).text,
                "description": self._find_child(i, self._item_description).text,
                "price": float(self._find_child(i, self._item_price).text[1:])
            })

        return items

    def remove_item(self, name):
        items = self._find_all(self._cart_item)
        for i in items:
            if self._find_child(i, self._item_name).text == name:
                self._find_child(i, self._remove_button).click()

        assert not [i['name'] for i in self.cart_items()], f"Failed to remove {name}, " \
                                                           f"still present in cart items"

    def proceed_to_customer_info_page(self):
        self._click(self._checkout_button)