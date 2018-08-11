student = {
  "first_name": "Pablo",
  "course": "CS101",
}

try:
  print("Trying to fetch invalid key")
  print(student.last_name)
except AttributeError as error:
  print("Caught AttributeError: {0}".format(error))
except TypeError as error:
  print("Caught TypeError: {0}".format(error))
except Exception as error:
  print("Uncaught Exception caught: {0}".format(error))
finally:
  print("Finally block ran")
