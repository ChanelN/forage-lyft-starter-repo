import sys

sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/car')
from car.car import Car
from abc import ABC, abstractmethod

#This engine class is supposed to be composition(not inheritance from car)- the 3 engines implement this through inheritence- 
class Engine(ABC):
    #this is the strategy interface
    def needs_service(self, *kwargs):
        #return super().baz(**kwargs)
        pass