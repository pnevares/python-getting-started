students = []


def get_students_titlecase():
  students_titlecase = []
  for student in students:
    students_titlecase.append(student["name"].title())
  return students_titlecase


def print_students_titlecase():
  students_titlecase = get_students_titlecase()
  print(students_titlecase)


def add_student(name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)

def save_file(student):
  try:
    f = open("students.txt", "a")
    f.write(student + "\n")
    f.close()
  except Exception:
    print("Exception trying to save file")

def read_file():
  try:
    f = open("students.txt", "r")
    for student in read_lines(f):
      add_student(student.rstrip("\n"))
    f.close()
  except Exception:
    print("Exception trying to read file")


def read_lines(f):
  for line in f:
    yield line


read_file()

while(True):
  choice = input("Do you want to enter another student? (yes/no): ")
  if choice == "no":
    break
  student_name = input("Enter student name: ")
  student_id = input("Enter student ID: ")
  add_student(student_name, student_id)
  save_file(student_name)

print("All student names:")
print_students_titlecase()
