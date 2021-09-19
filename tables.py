from dataclasses import dataclass
from typing import Any
from enum import Enum
from datetime import time, date


@dataclass
class Driver:
    id: int
    name: str
    rating: float
    phone: str
    car: str
    car_number: str


@dataclass
class Passenger:
    id: int
    name: str
    rating: float


class Tariff(Enum):
    ECONOM = "ECONOM"
    COMFORT = "COMFORT"
    COMFORT_PLUS = "COMFORT+"
    BUSINESS = "BUSINESS"


@dataclass
class Order:
    id: int
    address: str
    travel_date: date
    arrival_time: time
    waiting_time: time
    price: int
    driver: Driver
    passenger: Passenger
    tariff: Tariff

    def get_dict(self) -> dict[Any, Any]:
        return {
            "id": self.id,
            "address": self.address,
            "travel_date": self.travel_date,
            "arrival_time": self.arrival_time,
            "waiting_time": self.waiting_time,
            "price": self.price,
            "driver": self.driver.id,
            "passenger": self.passenger.id,
            "tariff": self.tariff,
        }
