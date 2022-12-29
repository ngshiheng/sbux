from dataclasses import dataclass


@dataclass
class Item:
    ItemId: str
    ItemCode: str
    Name: str
    Description: str
    BasePrice: int
    BasePriceDlvr: int
    PhotoURLs: list[str]
    Sequence: float
    ModifierGroup: list["ModifierGroup"]
    PMTNo: str
    PMTRefNo: str
    PMTAmount: int
    PMTLine: int
    IsMOP: bool
    IsDelivery: bool
    IsInventoried: bool
    IsFeatured: bool
    IsScheduled: bool
    IsDineIn: bool


@dataclass
class ModifierGroup:
    menu_id: str
    name: str
    description: str
    photo_urls: list[str]
    sequence: float
    selection_range_min: int
    selection_range_max: int
    is_fixed_price: bool
    is_free: bool
    is_quantifiable: bool
    uom: str
    modifiers: list["Modifier"]


@dataclass
class Modifier:
    ItemCode: str
    Name: str
    FilterCode: str
    UnitPrice: int
    UnitPriceDlvr: int
    Sequence: float
    SelectionRangeMin: int
    SelectionRangeMax: int
    IsFixedPrice: bool
    IsFree: bool
    IsQuantifiable: bool
    IsDefault: bool
    UOM: str
    PhotoURLs: list[str]
    DefaultKeys: list[str]
    DefaultValues: list[str]
