
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Name: {self.name} = {self.position}"
    

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions

employee1 = Employee("John Doe", "Manager")
print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Cook"))
print(employee1.get_info())



class Student:

    count = 0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += float(gpa)

    def get_info(self):
        return f"Name: {self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students available."
        return f"Average GPA: {round((cls.total_gpa / cls.count),3)}"
    
student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.5)
student3 = Student("Charlie", 3.9)

print(Student.get_count())
print(Student.get_average_gpa())