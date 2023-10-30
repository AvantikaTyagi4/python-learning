numbers = [1,3, 5,3, 35, 4, 8, 1,5]
uniques =[]
for number in numbers:
    if not number in uniques:
        uniques.append(number)
print(uniques)
