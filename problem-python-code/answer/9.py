#1
number = input()
dictionary = dict()
max_gifts = 0
max_person = None

for i in range(int(number)):
     name = input()
     if name in dictionary:
          dictionary[name] += 1
     else:
          dictionary[name] = 1
          
     if dictionary[name] > max_gifts:
          max_gifts = dictionary[name]
          max_person = name
          
print(max_person)

#2
from collections import defaultdict
number = input()
dictionary = defaultdict(lambda: 0)
max_gifts = 0
max_person = None

for i in range(int(number)):
     name = input()
     dictionary[name] += 1
     
     if dictionary[name] > max_gifts:
          max_gifts = dictionary[name]
          max_person = name
          
print(max_person)
