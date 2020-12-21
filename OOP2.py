class Employee:
    rais_ammount = 1.04
    num_of_emp = 0

    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.salary = salary
        Employee.num_of_emp += 1 

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_rais(self):
        self.salary = int(self.salary * self.rais_ammount)

emp_1 = Employee('safi','badi',120000)
emp_2 = Employee('John','Doe',10000)

#print(Employee.__dict__)
#print(emp_1.__dict__)

#Employee.rais_ammount = 1.05
#print(emp_1.rais_ammount)
#print(emp_2.rais_ammount)

#emp_1.rais_ammount = 1.05
#print(emp_1.rais_ammount)
#print(emp_2.rais_ammount)

print(Employee.num_of_emp)
print(emp_1.num_of_emp)



