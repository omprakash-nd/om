class Employee:
    empCount = 0

    def __init__(self, name, dept):

        self.name = name
        self.dept = dept
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d\n" %Employee.empCount

    def displayEmployee(self):
        print "Name:" , self.name ,"Department: ", self.dept

emp1 = Employee("om", 2000)
emp2 = Employee("prabu", 5000)
emp1.displayEmployee()
emp2.displayEmployee()        

class Company(Employee):
    def __init__(self, cid,branch):
        self.cid = cid
        self.branch = branch 

    def displayCompany(self):
        print "Company Id: ", self.cid, "Branch: ",self.branch
    
c = Company(1,"5G")
c.displayCompany()
c.displayCount()
