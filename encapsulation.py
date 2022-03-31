
# class to store methods to restrict other methods and variables from accedentlly altering the stored code
class Protected:
    # method containing a private variable
    def __init__(self):
        self.__privateVar = 12
    # method that prints variable
    def getPrivate(self):
        print(self.__privateVar)
    # asigning the private variable the tag 'private'
    def setPrivate(self, private):
        self.__privateVar = private
# calling class and its containing methods
obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()