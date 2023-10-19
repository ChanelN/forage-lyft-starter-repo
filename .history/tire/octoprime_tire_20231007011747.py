# serviced only when the sum of all values in the tire wear array is greater than or equal to 3
from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        sum = 0
        for number in self.tire_wear:
            sum += number
        if sum >= 3:
            return True
        return False