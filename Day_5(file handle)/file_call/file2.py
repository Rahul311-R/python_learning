import random
from file1 import greet, area_of_circle, safe_divide
#from file1 import *

# use custom functions
print(greet("Rahul"))

r = random.randint(1, 10)
print("Random radius:", r)
print("Area:", area_of_circle(r))

# test error handling
print(safe_divide(10, 2))
print(safe_divide(10, 0))
