class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll_no)
        print("Marks: ", self.marks)

class GraduateStudent(student):
    def __init__(self, name, roll_no, marks,project_name):
        super().__init__(name, roll_no, marks)
        self.project_name = project_name

    def display_graduate_details(self):
        self.display_details()
        print("Project Title: ", self.project_name)


student_list = {
    student("Tilak", 27, 94),
    student("Yash", 18, 92),
    student("Shikha", 23, 99)
}

for s in student_list:
    print("----------------------")
    s.display_details()

print("----------------------")
grad_student = GraduateStudent("Tilak", 27, 94, "AI System")
grad_student.display_graduate_details()