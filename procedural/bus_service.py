from . import vehicle_service # Inheritance replaced with import

repository = None # Dependency injection replaced with variable modification


def __get_bus(bus_id): # --> Encapsulation and abstraction of bus retrival
    return repository.get(bus_id)


def start_service(transport_id): # --> Polymorphism replaced with implicit contract
    bus = __get_bus(transport_id)
    vehicle_service.send_email_to_client(f'Bus with plate {bus.id} is being repaired')
