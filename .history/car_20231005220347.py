from datetime import datetime
from abc import ABC, abstractmethod
#abc = custom abstract base class, inherited but never instantiated so car itself can never be instantiated, only specific cars that inherit from t

#employee base class handles common interface payrollsystem(calculate_payroll)
#handles common interface
class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = None
        self.battery = None

    @abstractmethod
    #this is the strategy interface
    def needs_service(self):
        #pass or super? will i take it from class servicable?
        pass