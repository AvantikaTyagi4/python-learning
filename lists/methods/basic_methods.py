numbers = [1,3,2,5,10]

# to add any element at the last of list

numbers.append(40)
print(numbers)

# to add any element at particular index takes two parameter first is index of new element and second is element to insert
numbers.insert(2, 30)
print(numbers)

# to delete item from lsit pass the item to delete
numbers.remove(10)
print(numbers)

# to remove all the elements from list
numbers.clear()
print(numbers)

numbers = [1,3,2,5,10]
# to remove last item from list 
numbers.pop()
print(numbers)

# to check whether the item exist in list or not, if element exist in list it gives first index of element 
# but if element does not exist in list it gives error ValueError: 15 is not in lis
print(numbers.index(5))

# Another way to check the element exist in list or not is in it returns boolean value
print(20 in numbers)

numbers.append(5)
# to count the occurence of any element in the list
print(numbers.count(5))

# to sort the list
numbers.sort()
print(numbers)

# to sort the list in decending order 
numbers.sort()

# to reverese the list 
numbers.reverse()
print(numbers)


# to copy one list to another list
number2 = numbers.copy()
print(number2)