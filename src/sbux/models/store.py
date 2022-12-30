from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import LetterCase, config, dataclass_json


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class ServiceHour:
    day_of_week_string: Optional[str]
    day_of_week: Optional[int]
    open_from: Optional[str]
    open_to: Optional[str]
    is_24_hours: bool = field(metadata=config(field_name="Is24Hours"))
    is_closed: bool


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Amenities:
    nitro_cold_brew: bool
    starbucks_reserve: bool
    mobile_order_and_pay: bool = field(metadata=config(field_name="MobileOrderandPay"))
    free_wifi: bool
    pour_over_brew: bool


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Store:
    branch_code: Optional[str]
    outlet_code: Optional[str]
    store_code: Optional[str]
    store_name: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    phone_no: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]
    monp_status: bool = field(metadata=config(field_name="MONPStatus"))
    delivery_status: bool
    service_hours: list[ServiceHour]
    amenities: Amenities
