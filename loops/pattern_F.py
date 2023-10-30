# output 
# XXXXX
# XX
# XXXXX
# XX
# XX

numbers = [5,2,5,2,2]
# one way
for x_count in numbers:
    print('X' * x_count);

# using nested loop
for x_count in numbers:
    output =""
    for i in range(x_count):
        output += 'X'
    print(output)