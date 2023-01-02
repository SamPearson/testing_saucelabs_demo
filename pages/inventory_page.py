from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    _inventory_item = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _item_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _item_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _item_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _item_add_button = {"by": By.CLASS_NAME, "value": "btn_inventory"}

    def access_inventory_page(self):
        login_page = LoginPage(self.driver)
        login_page.access_login_page()
        login_page.login()
        # Asserting the inventory page has been reached is done in the login method

    def inventory(self):
        items = []
        item_elements = self._find_all(self._inventory_item)
        for i in item_elements:
            items.append({
                "name": self._find_child(i, self._item_name).text,
                "description": self._find_child(i, self._item_description).text,
                "price": self._find_child(i, self._item_price).text
            })

        return items

    def inventory_item(self, name):
        item_elements = self._find_all(self._inventory_item)
        for i in item_elements:
            if self._find_child(i, self._item_name).text == name:
                return i

        return False

    def add_item_to_cart(self, name):
        item = self.inventory_item(name)
        assert item, f"Cannot add item '{name}' to cart, item not found"
        self._find_child(item, self._item_add_button).click()
