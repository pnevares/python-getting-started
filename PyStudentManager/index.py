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

while(True):
  choice = input("Do you want to enter another student? (yes/no): ")
  if choice == "no":
    break
  student_name = input("Enter student name: ")
  student_id = input("Enter student ID: ")
  add_student(student_name, student_id)

print("Final list of students:")
print_students_titlecase()
