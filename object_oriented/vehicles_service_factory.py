from unittest.mock import Mock

from .bus import Bus
from .car import Car
from .bus_service import BusService
from .car_service import CarService


class VehiclesServiceFactory:
    @staticmethod
    def get_service(vehicle):
        fake_repository = Mock(get=Mock(return_value=vehicle))
        if isinstance(vehicle, Car):
            return CarService(fake_repository)
        
        if isinstance(vehicle, Bus):
            return BusService(fake_repository)

        return None
