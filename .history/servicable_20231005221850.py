from car import Car, abstractmethod

class Servicable():
    #the context is what chooses the types - so context is class that MAKES the actual car model
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

