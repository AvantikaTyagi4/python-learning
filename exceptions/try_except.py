# Code generating exception
# if user enter string for Age 
# we get ValueError: invalid literal for int() with base 10: 'xyz'
# age = int(input("Age: "))
# print(age)

# use try except to handle the error

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")