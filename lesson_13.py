add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

print(f"Six plus three equals {add(6, 3)}")
print(f"Six minus three equals {subtract(6, 3)}")
print(f"Six multiplied by three equals {multiply(6, 3)}")
print(f"Six divided by three equals {divide(6, 3)}")

adder = lambda x: lambda y: add(x, y)
addSeven = adder(7)
print(f"Three plus seven is {addSeven(3)}")
