from object_oriented.bus import Bus
from object_oriented.car import Car
from object_oriented.vehicles_service import VehiclesService
from object_oriented.vehicles_service_factory import VehiclesServiceFactory


vehicles = [
    Car(id=456, plate='PDGG2833'),
    Bus(id=123879),
]

for vehicle in vehicles:
    service: VehiclesService = VehiclesServiceFactory.get_service(vehicle)
    service.start_service(vehicle.id)
