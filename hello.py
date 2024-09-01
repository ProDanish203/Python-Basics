import math
import time

print("Hello, World!")

# username = "Danish Siddiqui"
# age = 21
# salaray = 250.50
# married = False

# print("Username: ", username, "Age: ", age, "Salary: ", salaray, "Married: ", married)

# Data Types / Object Types
# 1. Number (int, float, complex)
# 2. String (str)
# 3. List (list) [1, [2, "username"], 3.5, 4, 5]
# 4. Tuple (tuple) (1, "username", 3, 4, 5)
# 5. Dictionary (dict) {"username": "Danish", "age": 21, "salary": 250.50, "married": False}
#  6. Set (set) {1, 2, 3, 4, 5}
# 7. Boolean (bool) True, False
# 8. File (file) open("file.txt", "r")
# 9. None (None) None
# 10. Range (range) range(10)
# 11. Bytes (bytes) b"Hello, World!"
# 12. ByteArray (bytearray) bytearray(5)
# 13. Function (function) def sum(a, b): return a + b
# 14. Module (module) import math
# 15. Class (class) class Person: pass
# 16. Object (object) object()
# 17. Decorators, Generators, Iterators, MetaProgramming, etc.


# Conditionals In Python
# ages = [20, 17, 15, 21, 25, 30, 35, 40, 45, 50, 70, 60, 67, 85, 90, 95, 100]

# for age in ages:
#     if age < 13:
#         print("You are a child with age: ", age)
#     elif age >= 13 and age < 20:
#         print("You are a teenager with age: ", age)
#     elif age >= 20 and age < 60:
#         print("You are an adult with age: ", age)
#     elif age >= 60:
#         print("You are an old with age: ", age)
#     else:
#         print("Invalid age: ", age)


# Loops In Python
# numbers = [1, -4, 5, 8, 10, -7, -3, 0]
# for num in numbers:
#     if num >= 0:
#         print("Positive Number: ", num)
#     elif num < 0:
#         print("Negative Number: ", num)


# n = 10
# sum_even = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum_even += i

# print("Sum of Even Numbers: ", sum_even)

# Reverse a string using loop
# str = "Danish"
# strReverse = ""
# for char in str:
#     strReverse = char + strReverse

# print("Reverse String: ", strReverse)

# Factorial of a given number using while loop
# num = 5
# fact = 1
# while num > 0:
#     fact = fact * num
#     num = num - 1

# print("Factorial of ", num, " is: ", fact)


# Functions In Python
# def sum(a, b):
#     return a + b
# print(sum(2, 6))


# # Return multiple values from a function
# def calcCircAndArea(radius):
#     circumference = 2 * math.pi * radius
#     area = math.pi * radius * radius
#     return circumference, area


# circumference, area = calcCircAndArea(5)
# print("Circumference: ", round(circumference, 3), "Area: ", round(area, 3))

# # Default Arguments
# def greet(name="User"):
#     return "Hello, " + name + "!"

# print(greet("Danish"))
# print(greet())

# # Lambda Functions
# cube = lambda x: x**3
# print(cube(2))


# # *args functions
# def sum(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result


# print(sum(1, 2, 3, 4))

# # **kwargs functions
# def printData(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)


# printData(name="Danish", age=21, salary=250.50, married=False)


# # Recursion
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(5))


# # Object Oriented Programming In Python
# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand

#     def print_details(self):
#         return "Brand: ", self.__brand, "Model: ", self.__model

#     @staticmethod
#     def generate_report():
#         return "Total Cars: ", Car.total_car

#     # Read Only Property
#     @property
#     def model(self):
#         return self.__model


# # Inheritance
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def print_details(self):
#         return (
#             "Brand: ",
#             super().__brand,
#             "Model: ",
#             super().__model,
#             "Battery Size: ",
#             self.battery_size,
#         )


# car = Car("Toyota", "Corolla")
# # another_car = Car("Honda", "Civic")
# print(car.print_details())
# # Print private attributes
# # print(car.get_brand())
# # print("Total Cars: ", Car.total_car)
# # print(Car.generate_report())

# # car.model = "Camry"
# print(car.model)


# ev_car = ElectricCar("Tesla", "Model S", 100)
# # print(ev_car.print_details())

# print(isinstance(ev_car, ElectricCar))
# print(isinstance(ev_car, Car))


# # Decorators In Python
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print("Execution Time: ", end - start)
#         return result

#     return wrapper

# @timer
# def exm_function(n):
#     time.sleep(n)
#     print("Function Executed!")

# exm_function(2)


# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_values = [str(arg) for arg in args]
#         kwargs_values = [str(key) + "=" + str(value) for key, value in kwargs.items()]
#         print("Function Name: ", func.__name__)
#         print("Arguments: ", args_values, kwargs_values)
#         return func(*args, **kwargs)

#     return wrapper

# @debug
# def greet(name, greeting="Hello"):
#     print(greeting + ", " + name + "!")

# greet("Danish", greeting="Hi")

# def cache(func):
#     cache_value = {}
#     print("Cache Value: ", cache_value)

#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result

#     return wrapper


# @cache
# def long_running_task(a, b):
#     print("Task Started!")
#     time.sleep(2)
#     print("Task Completed!")
#     return a + b


# print(long_running_task(2, 3))
# print(long_running_task(2, 3))
# print(long_running_task(2, 4))
