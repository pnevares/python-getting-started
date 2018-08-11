def addOne(input):
  return input + 1

def add(first = 0, second = 0):
  return first + second

print(f"Five plus one is {addOne(5)}")
print(f"Six plus two is {add(6, 2)}")
print(f"Three plus zero is {add(3)}")
print(f"Zero plus zero is {add()}")
