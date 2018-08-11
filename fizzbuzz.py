for step in range(1, 101):
  output = ""

  if step % 3 == 0:
    output += "Fizz"
  
  if step % 5 == 0:
    output += "Buzz"
  
  if output == "":
    output = step

  print(output)
