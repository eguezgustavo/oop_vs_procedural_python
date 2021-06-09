from . import vehicle_service # Inheritance replaced with import

repository = None # Dependency injection replaced with variable modification


def __get_car(car_id): # --> Encapsulation and abstraction of car retrival
    return repository.get(car_id)


def start_service(transport_id): # --> Polymorphism replaced with implicit contract
    car = __get_car(transport_id)
    vehicle_service.send_email_to_client(f'Car with plate {car.plate} is being repaired')
