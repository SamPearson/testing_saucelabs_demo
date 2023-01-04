import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.inventory
class TestInventory:
    @pytest.fixture
    def inventory_page(self, driver):
        page = InventoryPage(driver)
        page.access_inventory_page()
        return page

    @pytest.mark.smoke
    def test_add_item_to_cart(self, inventory_page):
        num_cart_items = inventory_page.items_in_cart()

        items_not_in_cart = [i['name'] for i in inventory_page.inventory() if not i['in_cart']]
        item_to_add = items_not_in_cart[0]
        inventory_page.add_item_to_cart(item_to_add)

        assert item_to_add in inventory_page.items_in_cart()
        assert num_cart_items + 1 == inventory_page.items_in_cart()

    @pytest.mark.midweight
    def test_sorting(self, inventory_page):
        inventory_page.set_sorting_method('a to z')
        item_names = [i['name'] for i in inventory_page.inventory()]
        assert item_names == sorted(item_names)

        inventory_page.set_sorting_method('z to a')
        item_names = [i['name'] for i in inventory_page.inventory()]
        assert item_names == sorted(item_names, reverse=True)

        inventory_page.set_sorting_method('low to high')
        item_prices = [i['price'] for i in inventory_page.inventory()]
        assert item_prices == sorted(item_prices)

        inventory_page.set_sorting_method('high to low')
        item_prices = [i['price'] for i in inventory_page.inventory()]
        assert item_prices == sorted(item_prices, reverse=True)



