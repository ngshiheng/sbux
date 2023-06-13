# sbux

[![CI](https://github.com/ngshiheng/sbux/actions/workflows/ci.yml/badge.svg)](https://github.com/ngshiheng/sbux/actions/workflows/ci.yml)
[![Semantic Release](https://github.com/ngshiheng/sbux/actions/workflows/release.yml/badge.svg)](https://github.com/ngshiheng/sbux/actions/workflows/release.yml)

`sbux` is an unofficial Starbucks Singapore (SG) Python SDK.

## Installing

Install and update using `pip`;

```sh
pip install sbux
```

## Example

```python
from sbux import Starbucks


starbucks = Starbucks
starbucks.get_stores()
starbucks.get_menu_items(branch_code="13377")
```

See more [examples](./examples/).

## Contributing

For guidance on setting up a development environment and how to make a contribution, see the [contributing guidelines](./docs/CONTRIBUTING.md).
