#stores lots of data

# Data structure
# list, sets, tuples, dictionary

people = ["Jill", "Jean", "Irene","John","Betty"]
scores = [40,75,97,65,86]

#
# people.sort()
# scores.sort(reverse=True)
# print(people)
# print(scores)
#
# print(scores[0], scores[-1])
# print(sum(scores))
# print(sum(scores) / len(scores))

scores.sort()
# #slicing
# print(scores)
# print(scores[-3:])
# print(scores[:3])
# print(scores[3:5])

#set -- removes duplicates
numbers = {50,87,65,22,50}
print(numbers)

# Tuples --immutable data (never change)
days= ("Mon","Wed","Fri")
print(days[1])

#Dictionary
person= {"name": "Leon", "city": "New York", "age":36}
print(person["name"])

# data structures + algorithms
print(sum(numbers))
watu = [{"name":"Mary", "age": 33},
       {"name":"Jane", "age": 23},
       {"name":"Rahab", "age": 40}]
print(watu[1]["name" ])
