#Constructor is used for initializing object data.
#__init__():A constructor automatically called when an object is created.
class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
emp1=Employee("Rahul","2162")
print(emp1.name)
print(emp1.emp_id)