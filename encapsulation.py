# class using private attribute
class Private:
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
obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()



#class using protected attribute
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj2 = Protected()
obj2._protectedVar = 34
print(obj2._protectedVar)
