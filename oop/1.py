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

employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

employee1.display_info()
employee2.display_info()
print("total employee:", Employee.get_employee_count())
print("Is 50000 a valid salary?", Employee.is_valid_salary(50000))
print("Is -1000 a valid salary?", Employee.is_valid_salary(-1000))
