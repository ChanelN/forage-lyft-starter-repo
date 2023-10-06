from abc import ABC, abstractmethod
from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

#uses the factory design pattern (called client code)- decides what concrete implementation should be used
#cars created by calling a create method for each car model
class CarFactory:
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    '''
    @abstractmethod
    def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
        pass
    '''
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

'''
class create_calliope(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            #return Calliope()
            engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return engine or battery
        
class create_glissade(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            #return Glissade()
            engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
            battery = SpindlerBattery(last_service_date, current_date)
            return engine or battery
        
class create_palindrome(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            engine = SternmanEngine(last_service_date)
            battery = SpindlerBattery(last_service_date, current_date)
            return engine or battery
        
class create_rorschach(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return engine or battery

class create_thovex(CarFactory):
        #call with the specific engine and battery
        def create_car(current_date, last_service_date, current_mileage, last_service_mileage):
            #super().create_car(current_date, last_service_date, current_mileage, last_service_mileage)
            engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return engine or battery
'''