#serviced only when one or more values in the tire wear array >= 0.9
from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        for num in self.tire_wear:
            if num >= 0.9:
                return True
        return False