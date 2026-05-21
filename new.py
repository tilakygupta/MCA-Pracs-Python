class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks : ",self.marks)

students_list = {
            student("Tilak", 27, 94),
            student("Yash", 18, 92),
            student("Shikha", 23, 99)
        }

for s in students_list:
            print("----------------------")
            s.display_details()
