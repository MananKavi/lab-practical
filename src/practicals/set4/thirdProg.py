class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print("Total number of Employees are", Employee.empCount)

    def displayEmployee(self):
        print("Name :", self.name)
        print("Salary :", self.salary)


emp1 = Employee("Manan", 50000)
emp2 = Employee("Jananjay", 45000)
print("Employee.__doc__ :", Employee.__doc__)
print("Employee.__name__ :", Employee.__name__)
print("Employee.__module__ :", Employee.__module__)
print("Employee.__bases__ :", Employee.__bases__)
print("Employee.__dict__ :", Employee.__dict__)
