
class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation=designation
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary, "Designation: ", self.designation, )

class Manager(Employee): #manager inherits from employee
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation=designation
    def teamSize(self):
        size=int(input("Enter team size: "))
        print("Team Size: ", size)
        
class CXO(Manager):
    def __init__(self, name, salary, designation,shares,tenure):
        self.name = name
        self.salary = salary
        self.designation=designation
        self.shares=shares
        self.tenure=tenure
    def profitEarned(self):
        profit=(self.shares*self.salary)/100
        print("Profit: ", profit ,"%")
        

emp = Employee("Tom", 2000, "CTO")
man=Manager("Rom", 3000, "CEO")
cxo1=CXO("Paula",2000,"CTO",10,10)
cxo1.displayEmployee()
cxo1.teamSize()
cxo1.profitEarned()


