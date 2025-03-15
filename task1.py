from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


# Абстрактний клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас Car, що наслідує Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


# Клас Motorcycle, що наслідує Vehicle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# Абстрактна фабрика VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


# Фабрика для транспортних засобів у США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


# Фабрика для транспортних засобів у ЄС
class EUVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Використання фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()  # Ford Mustang (US Spec): Двигун запущено

vehicle2 = eu_factory.create_motorcycle("BMW", "750")
vehicle2.start_engine()  # BMW 750 (EU Spec): Мотор заведено
