# Student Class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"{self.name}'s Grades:")
        for assignment, grade in self.assignments.items():
            print(f" - {assignment}: {grade}")

# Instructor Class
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} to the course {self.course_name}.")

    def assign_grade(self, student, assignment_name, grade):
        if student in self.students:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"{student.name} is not enrolled in the course.")

    def display_all_students(self):
        print(f"Students in {self.course_name}:")
        for student in self.students:
            print(f" - {student.name} (ID: {student.student_id})")
            student.display_grades()

# Interactive Code
if __name__ == "__main__":
    # Create an instructor
    instructor = Instructor("Dr. Smith", "Python Programming")

    # Create students
    student1 = Student("John", 101)
    student2 = Student("Jane", 102)

    # Add students to the course
    instructor.add_student(student1)
    instructor.add_student(student2)

    # Assign grades
    instructor.assign_grade(student1, "Assignment 1", 85)
    instructor.assign_grade(student2, "Assignment 1", 90)

    # Display all students and their grades
    instructor.display_all_students()
