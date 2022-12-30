from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import LetterCase, config, dataclass_json


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Modifier:
    item_code: Optional[str]
    name: Optional[str]
    filter_code: Optional[str]
    unit_price: Optional[int]
    unit_price_dlvr: Optional[int]
    sequence: Optional[float]
    selection_range_min: Optional[int]
    selection_range_max: Optional[int]
    is_fixed_price: bool
    is_free: bool
    is_quantifiable: bool
    is_default: bool
    uom: Optional[str] = field(metadata=config(field_name="UOM"))
    photo_urls: Optional[list[str]] = field(metadata=config(field_name="PhotoURLs"))
    default_keys: Optional[list[str]]
    default_values: Optional[list[str]]


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class ModifierGroup:
    menu_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    photo_urls: Optional[list[str]] = field(metadata=config(field_name="PhotoURLs"))
    sequence: Optional[float]
    selection_range_min: Optional[int]
    selection_range_max: Optional[int]
    is_fixed_price: bool
    is_free: bool
    is_quantifiable: bool
    uom: Optional[str] = field(metadata=config(field_name="UOM"))
    modifiers: Optional[list[Modifier]]


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Item:
    item_id: Optional[str]
    item_code: Optional[str]
    name: Optional[str]
    description: Optional[str]
    base_price: Optional[int]
    base_price_dlvr: Optional[int]
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
