class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
 
    student_list.sort(key=lambda student: student.cgpa, reverse=True)


students = [
    Student("Clark Kent", "101", 3.9),
    Student("Barry Allen", "102", 3.5),
    Student("Bruce Wayne", "103", 4.0),
    Student("Diana", "104", 3.7),
    Student("Robin", "105", 3.8)
]


sort_students(students)


for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
