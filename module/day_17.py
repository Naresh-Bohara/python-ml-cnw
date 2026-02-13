## use of module
# from <module_name> import <function_name>

import module_example
print(module_example.add(5, 3))  # Output: 8
print(module_example.subtract(5, 3))  # Output: 2     
print(module_example.multiply(5, 3))  # Output: 15
print(module_example.divide(5, 3))  # Output: 1.666666
print(module_example.divide(5, 0))  # This will raise a ValueError: Cannot divide by zero.

# using alias for module
# import module_example as me
# print(me.add(10, 4))  # Output: 14

# import all functions from a module
# from module_example import *
# print(add(10, 4))  # Output: 14

# using alias for function
# from module_example import add as addition


### built in modules
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# random module
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and
# datetime module
import datetime
print(datetime.datetime.now())  # Output: Current date and time
# sys module
import sys
print(sys.version)  # Output: Python version information