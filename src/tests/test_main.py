import unittest
from unittest.mock import patch

from sbux import Starbucks
from sbux.models import Item, Store

from ._fixtures.item import ITEM_JSON
from ._fixtures.store import STORES_JSON


class StarbucksTestCase(unittest.TestCase):
    @patch("requests.get")
    def test_get_stores(self, mock_get):
        mock_get.return_value.json.return_value = STORES_JSON

        starbucks = Starbucks()
        stores = starbucks.get_stores()

        mock_get.assert_called_once_with(
            "https://static.sbux.mobi/json/mop/stores.json",
            headers={"user-agent": "starbucksSG/330 CFNEtwork/1399 Darwin/22.1.0"},
        )
        self.assertIsInstance(stores, list)
        self.assertEqual(len(stores), 2)
        self.assertTrue(all(isinstance(store, Store) for store in stores))

    @patch("requests.get")
    def test_get_menu_items(self, mock_get):
        mock_get.return_value.json.return_value = ITEM_JSON

        starbucks = Starbucks()
        store_id = "123"
        items = starbucks.get_menu_items(store_id)

        mock_get.assert_called_once_with(
            "https://static.sbux.mobi/json/mop/menu/123.json",
            headers={"user-agent": "starbucksSG/330 CFNEtwork/1399 Darwin/22.1.0"},
        )

        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 2)
        self.assertTrue(all(isinstance(item, Item) for item in items))
