class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute
    def __show_value(self):  # Private method
        print(self.__value)
    def public_method(self):  # Public method
        self.__show_value()  # Accessing private method within the class

# Usage
obj = MyClass(10)
# obj.__show_value()  # This would raise an AttributeError
# print(obj.__value)  # This would raise an AttributeError
obj.public_method()  # Accesses private method through a public method