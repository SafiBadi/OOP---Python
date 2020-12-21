class employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = employee('safi','badi',120000)

#print(emp1.email)

print(emp1.fullname())
print(employee.fullname(emp1))

