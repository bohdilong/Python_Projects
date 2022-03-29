class User:
    name = 'no name provided'
    email = ' '
    password = 'password'
    accountNumber = 0

class Employee(User):
    basePay = 25.00
    department = 'general'

class Customer(User):
    mailingAdderss = ' '
    mailingList = True
