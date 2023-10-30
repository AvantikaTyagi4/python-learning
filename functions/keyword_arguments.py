# keyword argument is used for increase the readability of program 
# or in this way we can also change the position of parameters while calling a function 
# If we want to use both keyword and postional arguments then first use postional argument followed by keyword arguments
# use keyword arguments for numerical arguments to increase the readibility

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')


print('Start')
greet_user(last_name="Smith",first_name="John") #function calling
print("End")

# If we want to use both keyword and postional arguments then first use postional argument followed by keyword arguments
greet_user("John",last_name="Smith")