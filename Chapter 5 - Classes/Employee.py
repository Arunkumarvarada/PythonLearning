class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept

    def displayEmployee(self):
        return(" Employee name is: "+self.name+" , Employee id is :"+str(self.id)+" and department where emp belongs to "+ self.dept)


"This is just basic example for creating classes and its syntaxes"
emp= Employee("Arun",122,"HPE")
print(emp.displayEmployee())

emp2= Employee("Varun",123,"HPE")
print(hasattr(emp2,"grade"))

setattr(emp2,"grade","A")
print(hasattr(emp2,"grade"))
print(getattr(emp2,"grade"))
print(getattr(emp2,"id"))
emp2.displayEmployee()
print(emp2.grade)
delattr(emp2,"grade")

# print(emp2.grade)