import unittest
import sys
sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/tire')
from carrigan_tire import CarriganTire
from octoprime_tire import OctoprimeTire

'''
Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
'''
class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        #one or more values in the tire wear array >= 0.9
        tire_wear = [0.1, 0.9, 1, 0.3]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        tire_wear = [0.1, 0.2, 0.1, 0.3]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1.0, 0.5, 1.0, 1.0]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
        
    def test_does_not_need_service(self):
        tire_wear = [0.3, 0.3, 0.2, 0.3]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
