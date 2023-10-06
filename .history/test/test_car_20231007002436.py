import unittest
from datetime import datetime
import sys

sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/engine')
from capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

#testing only concrete methods
class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced_1(self):
        current_mileage = 60001
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced_2(self):
        current_mileage = 80000
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced_1(self):
            current_mileage = 60000
            last_service_mileage = 30000
            car = CapuletEngine(current_mileage, last_service_mileage)
            self.assertFalse(car.needs_service(), "failed test 3")

    def test_engine_should_not_be_serviced_2(self):
        current_mileage = 50999
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service(), "failed test 4")

    def test_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service(), "failed test 5")

if __name__ == '__main__':
    unittest.main()
