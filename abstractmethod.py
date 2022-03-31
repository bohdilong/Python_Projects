from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print('your purchase amount: ',amount)
    @abstractmethod
    def payment(self, amount):
        pass

class DebtCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebtCardPayment()
obj.paySlip("$400")
obj.payment("$400")