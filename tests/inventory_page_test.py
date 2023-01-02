import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.inventory
class TestInventory:
    @pytest.fixture
    def inventory_page(self, driver):
        page = InventoryPage(driver)
        page.access_inventory_page()
        return page

    def test_add_to_cart(self, inventory_page):
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

