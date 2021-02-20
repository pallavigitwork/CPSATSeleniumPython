
class Student:
    def __init__(self,name,gender,age,marks):
        self.name=name
        self.gender=gender
        self.age=age
        self.marks=marks
    
    def printPercent(self):
        percent=(self.marks/500)*100
        print("Name: ", self.name, ", Percent: " , percent)

stud1=Student("Paul","Male",12,390)
stud1.printPercent()

stud2=Student("Rhea","Female",12,310)
stud2.printPercent()

