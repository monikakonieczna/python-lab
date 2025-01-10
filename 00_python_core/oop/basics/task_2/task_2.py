class SchoolMember:
    def __init__(self, name, age):
        """
        Initializes a school member with a name and age.

        :param name: The name of the school member.
        :param age: The age of the school member.
        """
        self.name = name
        self.age = age
    def show(self):
        """
        A placeholder method to be overridden by subclasses.

        :return: A string representation of the school member.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        """
        Initializes a student with a name, age, and grades.

        :param name: The name of the student.
        :param age: The age of the student.
        :param grades: The grades of the student.
        """
        super().__init__(name, age)
        self.salary = salary
    
    def show(self):
        """
        Returns a string representation of the teacher.

        :return: A string in the format "Name: <name>, Age: <age>, Salary: <salary>".
        """
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
class Student(SchoolMember):
    def __init__(self, name, age, grades):
        """
        Initializes a student with a name, age, and grades.

        :param name: The name of the student.
        :param age: The age of the student.
        :param grades: The grades of the student.
        """
        super().__init__(name, age)
        self.grades = grades
    
    def show(self):
        """
        Returns a string representation of the student.

        :return: A string in the format "Name: <name>, Age: <age>, Grades: <grades>".
        """
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"