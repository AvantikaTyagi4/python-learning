message = input(">")
# split method is used to convert string into list separed by the given character

words= message.split(' ')
print(words)

emojis={
    ":)":"Happy",
    ":(":"Sad"
}

output = ""
for word in words:
    output += emojis.get(word,word)+" "
print(output)
