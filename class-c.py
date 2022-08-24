class HumanBeing(object): #Inheritance (Parent class)
    def __init__(self,empName):
        self.empName=empName
class Employee(HumanBeing): # Inharitance (child class)
    def __init__(self,empName,empId,empSalary): 
        # super function is used to pass the empName attribute in parent class
        super().__init__(empName)
        self.empId=empId
        self.empSalary=empSalary
    def customer(self):
        return self.empName
        # __str__ is used to print the object
        # Normaly we print the object it returns a memory addrees
        # so we use __str__ to print the object what it returnss
    def __str__(self):
        return 'Name is:{}\n Salary is:{}\n'.format(self.empName, self.empSalary)
emp1=Employee('Thiru','1',25000)
print(emp1.customer())
print()
print(emp1)
