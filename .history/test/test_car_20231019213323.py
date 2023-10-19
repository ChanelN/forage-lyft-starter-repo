import unittest
import sys

#sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/engine')
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


#testing only concrete methods
class TestCapulet(unittest.TestCase):
    def capulet_should_be_serviced_1(self):
        current_mileage = 60001
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def capulet_should_be_serviced_2(self):
        current_mileage = 80000
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def capulet_should_not_be_serviced_1(self):
            current_mileage = 60000
            last_service_mileage = 30000
            car = CapuletEngine(current_mileage, last_service_mileage)
            self.assertFalse(car.needs_service(), "failed test 3")

    def capulet_should_not_be_serviced_2(self):
        current_mileage = 50999
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service(), "failed test 4")

    def capulet_should_not_be_serviced_3(self):
        current_mileage = 40000
        last_service_mileage = 30000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service(), "failed test 5")

class TestSternman(unittest.TestCase):
    def warning_light_on(self):
        warning_light_is_on = True
        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())
    def warning_light_off(self):
        warning_light_is_on = False
        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.needs_service())

class TestWilloughby(unittest.TestCase):
    def willoughby_should_be_serviced_1(self):
        current_mileage = 120001
        last_service_mileage = 60000
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def willoughby_should_be_serviced_2(self):
        current_mileage = 130000
        last_service_mileage = 60000
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def willoughby_should_not_be_serviced_1(self):
            current_mileage = 120000
            last_service_mileage = 60000
            car = WilloughbyEngine(current_mileage, last_service_mileage)
            self.assertFalse(car.needs_service())
            
    def willoughby_should_not_be_serviced_2(self):
        current_mileage = 110999
        last_service_mileage = 60000
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def willoughby_should_not_be_serviced_3(self):
        current_mileage = 60000
        last_service_mileage = 30000
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()