from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def Uppercase(string):
  return string.upper()

print(list(map(Uppercase, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))

scores = [73, 20, 65, 19, 76, 100, 88]
def is_pass(score):
  return score > 50

print(list(filter(is_pass, scores)))

def accumulator(acc, item):
  print(acc, item)
  return acc + item
print(reduce (accumulator,(my_numbers + scores)))