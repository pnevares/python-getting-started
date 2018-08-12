class Animal:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print("roar")

  def __str__(self):
    return self.name

bear = Animal("bear")
print(bear)
bear.talk()

human = Animal("human")
print(human)
human.talk()
