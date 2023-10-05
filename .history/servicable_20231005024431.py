from car import Car, abstractmethod

class Servicable():
    #the context is what chooses the types - so context is class that MAKES the actual car model
    def needs_service(self):
        print("needs service")