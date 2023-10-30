# parameterized function 
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')


print('Start')
greet_user("John","Smith") #function calling

# If we don't pass arguments in function calling TypeError: greet_user() missing 1 required positional argument: 'last_name' 
# greet_user("John")
print('End')