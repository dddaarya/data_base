from database import Database
from tables import Tariff
from datetime import date, time


if __name__ == "__main__":
    db = Database("database.json")
    # Заполняем инфу
    driver_a = db.insert_driver("Alex", 5.0, "89997775533", "Toyota", "A777XD")
    driver_b = db.insert_driver("Ben", 4.9, "89997775522", "BMW", "A666XD")
    driver_c = db.insert_driver("Chocoladka", 3.22, "89997775511", "LADA", "A555XD")
    passenger = db.insert_passenger("Passenger", 4.97)
    db.insert_order(
        "Kremlyovskaya 35",
        date(2020, 8, 3),
        time(5, 20),
        time(0, 3),
        240,
        driver_a,
        passenger,
        Tariff.ECONOM,
    )
    db.insert_order(
        "Kremlyovskaya 35",
        date(2020, 8, 3),
        time(8, 20),
        time(0, 4),
        690,
        driver_b,
        passenger,
        Tariff.BUSINESS,
    )
    db.insert_order(
        "Kremlyovskaya 35",
        date(2020, 8, 4),
        time(5, 20),
        time(0, 3),
        340,
        driver_c,
        passenger,
        Tariff.COMFORT,
    )
    # сохраняем
    db.save()
    # ищем и принтуем
    print(db.get_passenger_orders_on_date(passenger, date(2020, 8, 3)))
