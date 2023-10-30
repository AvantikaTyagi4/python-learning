course ="Python Tutorial for Begineer"
print(course[0])

# if we use -ve index then it gives character from last

print(course[-1])
print(course[-2])

# to print substring does not give character at last index
print(course[0:3])
print(course[5:9])

# if we do not pass end index it will give substring starting from start index to last character of string
print(course[1:])


# if we do not pass start index it will give substring starting from start index of actual string last index
print(course[:6])

# to get the whole string
print(course[:])

clone= course[:]
print(clone)

# if we write last index as negative it will skip number of character from last from the string
print(course[1:-2])