from abc import ABC, abstractmethod

class Servicable(ABC):
    #so serviceable is the service interface NOT the context
    '''
    def __init__(self, car:Car):
        self._car = car
    
    @property
    def car(self):
        #maintin reference to one of the Car(strategy interface?) objects
        return self._car
    
    @car.setter
    def car(self, car: Car):
        #to repllace car obj at runtime
        self._car = car

    def needs_service(self):
        print("needs service")
    '''
    @abstractmethod
    def needs_service(self):
        pass
