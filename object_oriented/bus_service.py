from .vehicles_service import VehiclesService


"""
Inhertitance and Polymorphism
Inherits the send_email_to_client method
Implements the start_service method
"""
class BusService(VehiclesService):
    def __init__(self, bus_repository): # --> Dependency Injection
        self.bus_repository = bus_repository
    
    def start_service(self, transport_id):
        bus = self.__get_bus(transport_id)
        self.send_email_to_client(f'Bus with id {bus.id} is being repaired')

    def __get_bus(self, bus_id): # --> Encapsulation and abstraction of car retrival
        return self.bus_repository.get(bus_id)
