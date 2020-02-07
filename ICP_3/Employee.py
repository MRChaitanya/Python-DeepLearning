class Employee:
    employee_count = 0
    employee_salary = 0

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.employee_count = Employee.employee_count + 1
        Employee.employee_salary = Employee.employee_salary + s

    def get_name(self):
        return self.name

    def get_family(self):
        return self.family

    def get_salary(self):
        return self.salary

    def get_department(self):
        return self.department

    def avg_salary(self):
        self.avg_salary = self.employee_salary / self.employee_count
        return self.avg_salary


class FulltimeEmployee(Employee):

    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)

e1 = FulltimeEmployee('Chaitanya', 'yes', 10000, 'cs')
print(e1.get_name())
print(e1.get_family())
print(e1.get_department())
print(e1.get_salary())
print(e1.avg_salary())


e2 = Employee('Raghu', 'yes', 50000, 'cs')
print(e2.get_name())
print(e2.get_family())
print(e2.get_department())
print(e2.get_salary())

print(e2.employee_count)

e3 = Employee('Raghu1', 'yes', 40000, 'cs')
print(e3.get_name())
print(e3.get_family())
print(e3.get_department())
print(e3.get_salary())
print(e3.avg_salary())

print(e3.employee_count)
