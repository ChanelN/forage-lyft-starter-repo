from abc import ABC

from car import Car

#derives from Car class - super initialised the 1 var from base class Car
# then this class defines current_mileage and last_service because of self.var = 
class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
