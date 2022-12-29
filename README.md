# sbux

`sbux` is an unofficial Starbucks Singapore (SG) software development kit (SDK). SBUX is the ticker symbol of Starbucks Corporation on the NASDAQ.

## Installing

Install and update using `pip`;

```sh
pip install sbux
```

## A Simple Example

```python
from sbux import Starbucks

app = Starbucks
app.get_stores()
app.get_menu_items(store_id="13377")
```

## Contributing

For guidance on setting up a development environment and how to make a contribution, see the [contributing guidelines](./docs/CONTRIBUTING.md).
