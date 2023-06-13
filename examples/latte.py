from sbux import Starbucks
from sbux.models import Item


def find_latte(items: list[Item]) -> Item:
    return next(item for item in items if item.name == "Caffè Latte")


def main():
    starbucks = Starbucks()

    for store in starbucks.get_stores():
        if not store.branch_code:
            continue

        items = starbucks.get_menu_items(store.branch_code)

        latte = find_latte(items)
        latte_price = latte.base_price / 100
        print(f"A cup of Caffè Latte at {store.store_name} costs ${latte_price:.2f}.")


if __name__ == "__main__":
    """$ python3 latte.py
    A cup of Caffè Latte at The Metropolis costs $6.60.
    A cup of Caffè Latte at Rochester Park costs $6.60.
    A cup of Caffè Latte at Paya Lebar Quarter costs $6.60.
    ...
    """
    main()
