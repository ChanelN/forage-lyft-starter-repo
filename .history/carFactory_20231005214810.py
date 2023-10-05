from abc import ABC, abstractmethod
from car import Car
from engine.engine import Engine
from battery.battery import Battery

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


#uses the factory design pattern (called client code)- decides what concrete implementation should be used
#cars created by calling a create method for each car model
class CarFactory(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @abstractmethod
    def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass


class create_calliope(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            return Calliope()
class create_glissade(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            return Glissade()
class create_palindrome(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            return Palindrome()
class create_rorschach(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            return Rorschach()
class create_thovex(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            return Thovex()