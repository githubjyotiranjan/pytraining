class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def printName(self):
        print("employee name", self.name)

    def printEmpDetails(self):
        print("employee details \n name:{},\n Age:{},\n Salary:{}".format(self.salary, self.age, self.salary))


emp = Employee("deepak", 35, 500000)
emp1 = Employee("Abhishek", 45, 50000)
emp.printName()
emp1.printEmpDetails()