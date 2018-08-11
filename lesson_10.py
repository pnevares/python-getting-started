contact = {
  "first_name": "Pablo",
  "last_name": "Nevares",
  "country": "USA"
}

print(contact)
print("Keys: {0}".format(contact.keys()))
print("Values: {0}".format(contact.values()))

keys = ["first_name", "country", "state"]

for key in keys:
  print("Looking for {0}:".format(key))
  print(contact.get(key, "key not found!"))

print("Deleting country")
del(contact["country"])
print(contact)
