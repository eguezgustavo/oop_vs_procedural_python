from procedural.bus import Bus
from procedural.car import Car
from procedural import vehicles_service_factory


vehicles = [
    Car(id=456, plate='PDGG2833'),
    Bus(id=123879),
]

for vehicle in vehicles:
    service = vehicles_service_factory.get_service(vehicle)
    service.start_service(vehicle.id)
