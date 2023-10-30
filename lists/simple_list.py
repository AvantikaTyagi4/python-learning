list =['Mark', 'Sarah','Josh','Kristen','Tom']

# to print entire list as it is 
print(list)

# to print first element of list
print(list[0])

# to print last element of list
print(list[-1])

# to print items from list from first index and skipping two items from last
print(list[1:-2])

# gives error since element is not present at given index   IndexError: list index out of range
# print(list[20])

# to modify any item of list
list [1] = 'Sara'
print(list)