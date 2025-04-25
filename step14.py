# 14. Aggregation

# Assignment:

# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

# Department class with aggregation
class Department:
    def __init__(self, department_name, employee: Employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department holds a reference to Employee

    def get_employee_details(self):
        return f"Department: {self.department_name}, Employee: {self.employee}"

# --- Testing Aggregation ---
emp1 = Employee("John Doe", "Software Engineer")
emp2 = Employee("Jane Smith", "Project Manager")

dept = Department("IT", emp1)

# Display details of the employee in the department
print(dept.get_employee_details())

# Create another department with a different employee
dept2 = Department("HR", emp2)
print(dept2.get_employee_details())
