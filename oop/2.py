from typing import ClassVar


class Employee:
    employee_count: ClassVar[int] = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary > 0


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def display_info(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


if __name__ == "__main__":
    employee1 = Employee("Alice", 50000)
    employee2 = Employee("Bob", 60000)
    manager1 = Manager("Charlie", 80000, "HR")

    employee1.display_info()
    employee2.display_info()
    manager1.display_info()
