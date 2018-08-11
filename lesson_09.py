files = ["README.md", "LICENSE", "CONTRIBUTORS.md"]
for file in files:
  print(f"checking {file}")
  if file == "LICENSE":
    print("Found LICENSE")
    break

index = 0
while True:
  print("index is {0}".format(index))
  if index == 4:
    break
  index += 1
print("out of while loop")
