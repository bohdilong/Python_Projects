from abc import ABC, abstractmethod


class car(ABC):
    #this function prints how much your purchase was
    def paySlip(self, amount):
        print('your purchase amount: ',amount)
    #this function is asking to pass in a an aurgument    
    @abstractmethod
    def payment(self, amount):
        pass

class DebtCardPayment(car):
    
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebtCardPayment()
obj.paySlip("$400")
obj.payment("$400")