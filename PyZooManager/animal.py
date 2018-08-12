def save_file(animal):
  try:
    f = open("animals.txt", "a")
    f.write(animal + "\n")
    f.close()
  except Exception as e:
    print("Exception trying to save file: {0}".format(e))

def read_file():
  animals = []
  try:
    f = open("animals.txt", "r")
    for animal in f.readlines():
      animals.append({"type": animal.rstrip("\n"), "count": 1})
    f.close()
    return animals
  except Exception as e:
    print("Exception trying to read file: {0}".format(e))
    return []
