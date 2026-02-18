### Example of access_control in Python using inheritance
class Demo:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def show_public(self):
        print(self.public_var)
    def show_protected(self):
        print(self._protected_var)
    def __show_private(self):
        print(self.__private_var)
    
    def show_private_outside(self):
        self.__show_private()  # Accessing private method within the class

demo = Demo()
demo.show_public()  # Output: I am public
demo.show_protected()  # Output: I am protected
demo.show_private_outside()  # Output: I am private
# Accessing private variable outside the class will raise an AttributeError
# print(demo.__private_var)  # This will raise an AttributeError
# demo.__show_private()  # This will raise an AttributeError because it's a private method
