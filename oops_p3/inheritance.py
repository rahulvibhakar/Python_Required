#In Inheritance child class inherit properties from parent class. Here Person is Parent class and Employee is child class and we use methods.
class Person:
    def display(self):
        print("Person")
class Employee(Person):
    pass
emp=Employee()
emp.display()