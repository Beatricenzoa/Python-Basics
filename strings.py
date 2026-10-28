name="Noel"
sentence= "It is very cold today in \"xyz\"" # escape character
print(sentence)

#operations
print(name.upper())
print(name)
name= name.upper()

print(name)
print(sentence.capitalize())
print(sentence.title())

print(sentence.count("M")) #call in function using a parameter
print(len(sentence))
print(len(name))
replaced_sentence = sentence.lower().replace("cold", "hot")
print(replaced_sentence)

m= "123"
sentence.isnumeric()

print(name.isnumeric())