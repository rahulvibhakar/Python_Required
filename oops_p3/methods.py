#display() is method here.
class Employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
emp1=Employee("Rahul")
emp1.display();