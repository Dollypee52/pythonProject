class Animal:
  def __init__(self,name,age=0):
    self.name = name
    self.age = age

  def speak(self):
    return "Animal speak"


class Dog(Animal):
  def __init__(self, type_, name, age):
    print("From Dog")
    super().__init__(name, age)
    self.type = type_

  def speak(self):
     super().speak()
     return "Dog speak"



class Cat(Animal):
  pass

class Bingo(Dog, Cat):
  pass


dog =Dog("Bingo","local", 2)
cat =Cat("Kitty")

print(dog.speak())
print(dog.name)
print(dog.type)
# print(Cat.name)
print(f"my name is {dog.name} and i  ")


# print(cat.name)







