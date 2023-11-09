from dataclasses import dataclass, field

from dataclasses_json import config

from .base import BaseSBUXDataClassJsonMixin


@dataclass
class ServiceHour(BaseSBUXDataClassJsonMixin):
    """Represents the operating hours of a Starbucks store on a particular day of the week."""

    day_of_week_string: str
    day_of_week: int
    open_from: str
    open_to: str
    is_24_hours: bool = field(metadata=config(field_name="Is24Hours"))
    is_closed: bool


@dataclass
class Amenities(BaseSBUXDataClassJsonMixin):
    """Represents the amenities available at a Starbucks store."""

    nitro_cold_brew: bool
    starbucks_reserve: bool
    mobile_order_and_pay: bool = field(metadata=config(field_name="MobileOrderandPay"))
    free_wifi: bool
    cashless: bool
    twenty_four_hours: bool = field(metadata=config(field_name="24Hours"))


@dataclass
class Store(BaseSBUXDataClassJsonMixin):
    """Represents a Starbucks store."""

    branch_code: str
    outlet_code: str
    store_code: str
    store_name: str
    address: str
    postal_code: str
    phone_no: str
    longitude: str
    latitude: str
    monp_status: bool = field(metadata=config(field_name="MONPStatus"))
    delivery_status: bool
    open_now: bool
    service_hours: list[ServiceHour]
    amenities: Amenities
