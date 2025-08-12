class Employee:
 employee_list = []
 def __init__(self, name, salary):
   self.name = name
   self.salary = salary
   Employee.employee_list.append(self)

 def display_info(self):
    print(f"Name: {self.name}, Salary: {self.salary}")

 @classmethod
 def get_employee_count(cls):
    return len(cls.employee_list)

 @staticmethod
 def is_valid_salary(salary):
   if salary > 0:
    return True
   else:
    return False
   
class Manager(Employee):
  def __init__(self, name, salary, department):
    super().__init__(name,salary)
    self.department = department

  def display_info(self):
    print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

manager1 = Manager("Charlie", 80000, "HR")    

employee1.display_info()
employee2.display_info()
manager1.display_info()
