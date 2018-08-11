students = []


def get_students_titlecase():
  students_titlecase = []
  for student in students:
    students_titlecase = student["name"].title()
  return students_titlecase


def print_students_titlecase():
  students_titlecase = get_students_titlecase()
  print(students_titlecase)


def add_student(name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)


student_list = get_students_titlecase()
print(student_list)

add_student("Mark")
student_list = get_students_titlecase()
print(student_list)
