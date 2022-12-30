import requests

from .models import Item, Store


class Starbucks:
    """The main class to instantiate to access Starbucks API."""

    def __init__(self):
        self.api_base_url = "https://static.sbux.mobi"
        self.headers = {"user-agent": "starbucksSG/330 CFNEtwork/1399 Darwin/22.1.0"}

    def get_stores(self) -> list[Store]:
        """Retrieves a list of stores from the Starbucks API."""
        url = f"{self.api_base_url}/json/mop/stores.json"
        response = requests.get(url, headers=self.headers)

        return self._parse_get_stores(response)

    def _parse_get_stores(self, response: requests.Response) -> list[Store]:
        """Parses the response from a 'get_stores' request and returns a list of Store objects."""
        stores_data = response.json()["Data"]

        return Store.schema().load(stores_data, many=True)

    def get_menu_items(self, branch_code: str) -> list[Item]:
        """Retrieves a list of menu items for a given BranchCode from the Starbucks API."""
        is_valid_branch_code = (
            branch_code and isinstance(branch_code, str) and branch_code.isnumeric()
        )
        if not is_valid_branch_code:
            raise ValueError("Invalid input. branch_code must be a valid string numeric.")

        url = f"{self.api_base_url}/json/mop/menu/{branch_code}.json"
        response = requests.get(url, headers=self.headers)

        return self._parse_get_menu_items(response)

    def _parse_get_menu_items(self, response: requests.Response) -> list[Item]:
        """Parses the response from a 'get_menu_items' request and returns a list of Item objects."""
        menu_data = response.json()["Data"][0]["Items"]

        return Item.schema().load(menu_data, many=True)
