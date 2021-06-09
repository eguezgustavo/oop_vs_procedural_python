from .vehicles_service import VehiclesService


"""
Inhertitance and Polymorphism
Inherits the send_email_to_client method
Implements the start_service method
"""
class CarService(VehiclesService):
    def __init__(self, car_repository): # --> Dependency Injection
        self.car_repository = car_repository
    
    def start_service(self, transport_id):
        car = self.__get_car(transport_id)
        self.send_email_to_client(f'Car with plate {car.plate} is being repaired')

    def __get_car(self, car_id): # --> Encapsulation and abstraction of car retrival
        return self.car_repository.get(car_id)
