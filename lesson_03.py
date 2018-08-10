print('Hello world' == "Hello world")
print("hello".capitalize() == "Hello")
print("hello".upper() == "HELLO")
print("hello".replace("e", "a") == "hallo")
print("hello".isalpha() == True)
print("123".isdigit() == True)
print("some,more,values".split(",") == ["some", "more", "values"])

print("Hello {0}, welcome to {1}".format("Dave", "space"))

where = "down"
what = "reverse"
print(f"I put my thing {where}, flip it, and {what} it")