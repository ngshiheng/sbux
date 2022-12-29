from dataclasses import dataclass


@dataclass
class Store:
    BranchCode: str
    OutletCode: str
    StoreCode: str
    StoreName: str
    Address: str
    PostalCode: str
    PhoneNo: str
    Longitude: str
    Latitude: str
    MONPStatus: bool
    DeliveryStatus: bool
    ServiceHours: list["ServiceHour"]
    Amenities: "Amenities"


@dataclass
class ServiceHour:
    DayOfWeekString: str
    DayOfWeek: int
    OpenFrom: str
    OpenTo: str
    Is24Hours: bool
    IsClosed: bool


@dataclass
class Amenities:
    NitroColdBrew: bool
    StarbucksReserve: bool
    MobileOrderandPay: bool
    FreeWifi: bool
    PourOverBrew: bool
