# dictionary in python is used to store data in key value pairs
# keys must be unique

customer={
    "name":"John Smith",
    "age": 30,
    "is_verified": True
}

# to get the value of key
print(customer["name"])

# if the key does not exist in Dictionary it gives Keyerror and it is case sesitive
# KeyError: 'birthday'
# print(customer['birthday'])

# Another way to get the value of key to use get method
print(customer.get("name"))

# If key does not exist it will give None 
# None is something which is not known remember empty and None are different
# None is an object that represents the absence of a value
print(customer.get("Name"))

# to pass the default value to key if it does not exist but it won't modify the dictionary
print(customer.get("birthdate", "20 Jan 1990"))

print(customer)

# to modify the value of existing key
customer["name"] = "Jack Smith"
print(customer["name"])

# to add new key value pair
customer["birthdate"] = "20 Jan 1990"
print(customer["birthdate"])