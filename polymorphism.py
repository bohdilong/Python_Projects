# parent class
class User:
    name = "Jose"
    email = "example@gmail.com"
    password = "123asd"

    def login_info(self):
        get_name = input("enter your name: ")
        get_email = input("enter your email: ")
        get_password = input("enter your password: ")
        if (get_email == self.email and get_email == self.password):
            print("Welcome {}!".format(get_name))
        else:
            print("Your email or password is wrong!")


#child class Employee
class Employee(User):
    Pay = 25.00
    department = "General"
    pinNum = "4321"

# same method as user but with pin instead of password
    def login_info(self):
        get_name = input("enter your name: ")
        get_email = input("enter your email: ")
        get_password = input("enter your pin: ")
        if (get_email == self.email and get_email == self.password):
            print("Welcome {}!".format(get_name))
        else:
            print("Your email or pin is wrong!")


# invokes methods inside class user
guest = User()
guest.login_info()


manager = Employee()
manager.login_info()
