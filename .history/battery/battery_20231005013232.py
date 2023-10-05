from car import Car
from abc import ABC, abstractmethod

#also uses composition. Car HAS-A battery
class Battery():
    #this is the strategy interface
    def needs_service(self, *kwargs):
        return super().baz(**kwargs)