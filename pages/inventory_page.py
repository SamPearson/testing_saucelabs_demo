from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    _inventory_item = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _item_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _item_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _item_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _item_add_button = {"by": By.CLASS_NAME, "value": "btn_inventory"}

    _cart_link = {"by": By.CLASS_NAME, "value": "shopping_cart_link"}
    _cart_badge = {"by": By.CLASS_NAME, "value": "shopping_cart_badge"}

    _active_sorting_method = {"by": By.CLASS_NAME, "value": "active_option"}
    _sort_method_menu = {"by": By.CLASS_NAME, "value": "product_sort_container"}
    _sort_menu_option = {"by": By.TAG_NAME, "value": "option"}

    def access_inventory_page(self):
        login_page = LoginPage(self.driver)
        login_page.access_login_page()
        login_page.login()
        # Asserting the inventory page has been reached is done in the login method

    def inventory(self):
        items = []
        item_elements = self._find_all(self._inventory_item)
        for i in item_elements:
            item_in_cart = False
            cart_button_text = self._find_child(i, self._item_add_button).text
            if 'remove' in cart_button_text.lower():
                item_in_cart = True
            items.append({
                "name": self._find_child(i, self._item_name).text,
                "description": self._find_child(i, self._item_description).text,
                "price": float(self._find_child(i, self._item_price).text[1:]),
                "in_cart": item_in_cart
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

    def items_in_cart(self):
        badge_element = self._find(self._cart_badge)
        if badge_element:
            return int(badge_element.text)
        return 0

    def active_sorting_method(self):
        return self._find(self._active_sorting_method).text

    def set_sorting_method(self, sorting_method):
        sorting_method = sorting_method.lower()
        option_names = [
            'a to z',
            'z to a',
            'low to high',
            'high to low'
        ]
        assert sorting_method in option_names, f"Sorting method must be one of the following: " \
                                               f"{option_names}"

        menu = self._find(self._sort_method_menu)
        menu.click()
        for option in self._find_children(menu, self._sort_menu_option):
            if sorting_method in option.text.lower():
                option.click()
                return

        raise AssertionError(f'Could not find sorting method {sorting_method}')
