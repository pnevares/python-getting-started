class Animal:
  planet = "Earth"

  def __init__(self, name):
    self.name = name

  def talk(self):
    print("roar")

  def __str__(self):
    return f"{self.name} on {self.planet}"

bear = Animal("bear")
print(bear)
bear.talk()

human = Animal("human")
print(human)
human.talk()

print(Animal.planet)
