import unittest
from datetime import date

import sys
sys.path.insert(0, '/Users/gautamgrg/Documents/forage-lyft-starter-repo/battery')
from nubbin_battery import NubbinBattery
from spindler_battery import SpindlerBattery

class TestNubbin(unittest.TestCase):
    #every 4 years
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindler(unittest.TestCase):
    #every 2 years
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-03-11")
        last_service_date = date.fromisoformat("2021-03-11")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-03-11")
        last_service_date = date.fromisoformat("2022-03-11")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())