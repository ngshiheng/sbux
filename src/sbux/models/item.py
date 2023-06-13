from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config

from .base import BaseSBUXDataClassJsonMixin


@dataclass
class Modifier(BaseSBUXDataClassJsonMixin):
    """Represents a menu item modifier at Starbucks."""

    item_code: str
    name: str
    filter_code: Optional[str]
    unit_price: int
    unit_price_dlvr: int
    sequence: float
    selection_range_min: int
    selection_range_max: int
    is_fixed_price: bool
    is_free: bool
    is_quantifiable: bool
    is_default: bool
    uom: Optional[str] = field(metadata=config(field_name="UOM"))
    photo_urls: Optional[list[str]] = field(metadata=config(field_name="PhotoURLs"))
    popup_image: bool
    default_keys: Optional[list[str]]
    default_values: Optional[list[str]]
    description: Optional[str]


@dataclass
class ModifierGroup(BaseSBUXDataClassJsonMixin):
    """Represents a group of modifiers that can be applied to a menu item at Starbucks."""

    menu_id: str
    name: str
    description: str
    photo_urls: Optional[list[str]] = field(metadata=config(field_name="PhotoURLs"))
    sequence: Optional[float]
    selection_range_min: Optional[int]
    selection_range_max: Optional[int]
    is_fixed_price: bool
    is_free: bool
    is_quantifiable: bool
    uom: Optional[str] = field(metadata=config(field_name="UOM"))
    modifiers: Optional[list[Modifier]]


@dataclass
class Item(BaseSBUXDataClassJsonMixin):
    """Represents a menu item at Starbucks."""

    item_id: str
    item_code: Optional[str]
    name: str
    description: Optional[str]
    base_price: int
    base_price_dlvr: int
    photo_urls: Optional[list[str]] = field(metadata=config(field_name="PhotoURLs"))
    sequence: Optional[float]
    modifier_group: Optional[list[ModifierGroup]]
    pmt_no: Optional[str] = field(metadata=config(field_name="PMTNo"))
    pmt_ref_no: Optional[str] = field(metadata=config(field_name="PMTRefNo"))
    pmt_amount: Optional[int] = field(metadata=config(field_name="PMTAmount"))
    pmt_line: Optional[int] = field(metadata=config(field_name="PMTLine"))
    is_mop: bool = field(metadata=config(field_name="IsMOP"))
    is_delivery: bool
    is_inventoried: bool
    is_featured: bool
    is_scheduled: bool
    is_dine_in: bool
