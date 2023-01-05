from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutConfirmPage(BasePage):
    _checkout_summary_container = {"by": By.ID, "value": "checkout_summary_container"}

    _cart_item = {"by": By.CLASS_NAME, "value": "cart_item"}
    _item_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _item_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _item_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}

    _checkout_button = {"by": By.ID, "value": "finish"}

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

    def complete_checkout(self):
        self._click(self._checkout_button)