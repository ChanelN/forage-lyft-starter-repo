import unittest
import sys
sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/tire')
from carrigan_tire import CarriganTire
from octoprime_tire import OctoprimeTire

class TestCarrigan(unittest.TestCase):
    def test_needs_service(self):
        #one or more values in the tire wear array >= 0.9
        tire_wear = [0.1, 0.9, 1, 0.3]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service(), "tire need service")