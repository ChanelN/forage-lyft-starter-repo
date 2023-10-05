from abc import ABC, abstractmethod
from calliope import Calliope
from glissade import Glissade
from palindrome import Palindrome
from rorschach import Rorschach
from thovex import Thovex

#uses the factory design pattern (called client code)- decides what concrete implementation should be used
#cars created by calling a create method for each car model
class CarFactory(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope #or is it car= new calliope
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        return Palindrome
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return  Thovex