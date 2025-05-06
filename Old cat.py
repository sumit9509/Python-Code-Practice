class Cat:
  species = 'mammal'
  def __init__(self, name, age):
      self.name = name
      self.age = age

cat1 = Cat('Tom', 12)
cat2 = Cat('Jackie', 15)
cat3 = Cat('Tiger', 10)

def old(*args):
    return max(args)
    
print(f' The oldest Cat is {old(cat1.age, cat2.age, cat3.age)} years old')
    

