# Employee Class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")

# Department Class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee {employee.name} to department {self.department_name}.")

    def calculate_total_salary(self):
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()

# Interactive Code
if __name__ == "__main__":
    # Create a department
    department = Department("Software Engineering")

    # Create employees
    emp1 = Employee("Alice", 1, 70000)
    emp2 = Employee("Bob", 2, 85000)

    # Add employees to the department
    department.add_employee(emp1)
    department.add_employee(emp2)

    # Display all employees
    department.display_all_employees()

    # Calculate total salary expenditure
    department.calculate_total_salary()
