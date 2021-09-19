from dataclasses import dataclass, field
from tables import Driver, Passenger, Order, Tariff
from datetime import time, date
import json


@dataclass
class Database:
    """Простая файловая БД. На данном этапе не предусматривает удаление записей."""

    filename: str
    _drivers: list[Driver] = field(init=False, default_factory=list)
    _passengers: list[Passenger] = field(init=False, default_factory=list)
    _orders: list[Order] = field(init=False, default_factory=list)

    def insert_driver(
        self, name: str, rating: float, phone: str, car: str, car_number: str
    ) -> Driver:
        driver = Driver(
            id=len(self._drivers),
            name=name,
            rating=rating,
            phone=phone,
            car=car,
            car_number=car_number,
        )
        self._drivers.append(driver)
        return driver

    def insert_passenger(self, name: str, rating: float) -> Passenger:
        passenger = Passenger(id=len(self._passengers), name=name, rating=rating)
        self._passengers.append(passenger)
        return passenger

    def insert_order(
        self,
        address: str,
        travel_date: date,
        arrival_time: time,
        waiting_time: time,
        price: int,
        driver: Driver,
        passenger: Passenger,
        tariff: Tariff,
    ) -> Order:
        order = Order(
            id=len(self._orders),
            address=address,
            travel_date=travel_date,
            arrival_time=arrival_time,
            waiting_time=waiting_time,
            price=price,
            driver=driver,
            passenger=passenger,
            tariff=tariff,
        )
        self._orders.append(order)
        return order

    def save(self) -> None:
        save_dict = {
            "drivers": [x.__dict__ for x in self._drivers],
            "passengers": [x.__dict__ for x in self._passengers],
            "orders": [x.get_dict() for x in self._orders],
        }
        with open(self.filename, "w+") as json_file:
            json.dump(save_dict, json_file, default=str)

    def load(self) -> None:
        raise NotImplementedError()

    def get_passenger_orders_on_date(
        self, passenger: Passenger, filter_date: date
    ) -> list[Order]:
        filt = lambda x: x.passenger.id == passenger.id and filter_date == x.travel_date
        return list(filter(filt, self._orders))