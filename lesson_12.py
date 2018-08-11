def add_one(input):
  return input + 1


def add(first = 0, second = 0):
  return first + second


def print_var_args(first, *args):
  print(first)
  print(args)

def print_kw_args(first, **args):
  print(first)
  print(args)

print(f"Five plus one is {add_one(5)}")
print(f"Six plus two is {add(6, 2)}")
print(f"Three plus zero is {add(3)}")
print(f"Zero plus zero is {add()}")

print_var_args("first arg", "second arg", "third arg", "fourth arg")
print_kw_args("first arg", second="second arg", third="third arg", fourth="fourth arg")
