from typing import ClassVar

class Employee:
    # Class variable to keep track of total employees
    employee_count: ClassVar[int] = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name             # Instance variable for employee name
        self.salary = salary         # Instance variable for employee salary
        Employee.employee_count += 1

    def display_info(self) -> None:
        """Instance method to display employee info"""
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def get_employee_count(cls) -> int:
        """Class method to get total number of employees"""
        return cls.employee_count

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        """Static method to check if salary is valid"""
        return salary > 0


# Demonstrate functionality
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

employee1.display_info()
employee2.display_info()

print("Total employees:", Employee.get_employee_count())
print("Is 50000 a valid salary?", Employee.is_valid_salary(50000))
print("Is -1000 a valid salary?", Employee.is_valid_salary(-1000))
