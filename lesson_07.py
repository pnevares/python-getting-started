colors = ["red", "green", "blue"]
print(colors[0])

colors.append("yellow")
print(colors[-1])

if "blue" in colors:
  print("blue is a color")
else:
  print("blue is not a color")

print(f"there are {len(colors)} colors:")
print(colors)

print(f"deleting last color {colors[-1]}")
del colors[-1]

print(f"there are {len(colors)} colors:")
print(colors)
