# parent class
class User:
    name = 'no name provided'
    email = ' '
    password = 'password'
    accountNumber = 0


# child class employee
class Employee(User):
    basePay = 25.00
    department = 'general'


# child class customer
class Customer(User):
    mailingAdderss = ' '
    mailingList = True
