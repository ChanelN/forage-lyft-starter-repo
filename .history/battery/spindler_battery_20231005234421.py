from abc import ABC
from battery.battery import Battery
from dateutil import relativedelta

#Implements Battery
#inherit from Battery not Car
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        #super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        #assuming that the dates are already in datetime format, not string
        delta = relativedelta.relativedelta(self.current_date, self.last_service_date)
        return delta.years > 2