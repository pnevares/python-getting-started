class Animal:
  planet = "Earth"

  def __init__(self, name):
    self.name = name

  def talk(self):
    print("roar")

  def __str__(self):
    return f"{self.name} on {self.planet}"


class AlienAnimal(Animal):
  planet = "Mars"

  def talk(self):
    super().talk()
    print("...xyzzy")
