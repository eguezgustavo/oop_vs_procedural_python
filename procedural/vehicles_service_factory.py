from unittest.mock import Mock

from .bus import Bus
from .car import Car
from . import bus_service
from . import car_service


def get_service(vehicle):
    if isinstance(vehicle, Car):
        car_service.repository = Mock(get=Mock(return_value=vehicle))
        return car_service
    
    if isinstance(vehicle, Bus):
        bus_service.repository = Mock(get=Mock(return_value=vehicle))
        return bus_service

    return None
