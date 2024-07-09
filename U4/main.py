'''Employee
-id:int
-firstName:String
-lastName:String
-salary:int

+Employee(id:int,firstName:String,lastName:String,salary:int)
+getID():int
+getFirstName():String
+getLastName():String
+getName():String
+getSalary():int
+setSalary(salary:int):void
+getAnnualSalary():int
+raiseSalary(int percent):int
+toString():String

"firstName lastname"

salary * 12

Increase the salary by the percent and return the new salary

"Employee[id=?,name=firstName lastname,salary=?]"

3. Employee nomli klass yarating. Unda quyidagi rasmda ko’rsatilgan atribut va metodlarni yarating.'''

class Employee:
    def __init__(self, ID:int, first_name:str, last_name:str, salary:int):
        self.ID = ID
        self.name = first_name
        self.last_name = last_name
        self.salary = salary

    def employee(self):
        return f"Name: {self.name} LastName: {self.last_name} ID: {self.ID} Salary {self.salary}$"
    
    def get_id(self):
        return f"ID: {self.ID}"
    
    def get_First_name(self):
        return f"FirstName: {self.name}"
    
    def get_last_name(self):
        return f"Last_name: {self.last_name}"


    def get_name(self):
        return f"Name: {self.name} {self.last_name}"
    
    def salary_per_month(self):
        return f"Salary: {self.salary}$"
    
    def set_salary(self, new_salary:int):
        self.salary = new_salary
        print(f"Your salary is changed {self.salary}$")

    def get_annualy(self):
        return f"Anually salary: {self.salary * 12}$"


    def raise_salary(self, percent:int):
        return f"Raised salary: {self.salary + ((self.salary / 100) * percent)}$"
    
    def toString(self):
        return [self.name, self.last_name,  str(self.ID), str(self.salary) + '$']

user = Employee(12421, "Abdulloh", "Mirzaholiqov", 5000)
# print(user.get_annualy())
# print(user.toString())
# print(user.raise_salary(20))
# user.set_salary(4500)
# print(user.salary_per_month())
# print(user.get_First_name())
# print(user.get_last_name())
# print(user.get_name())
# print(user.get_id())
# print(user.employee())




