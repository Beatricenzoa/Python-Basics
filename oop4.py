# inheritance
# employee - name, id,gender,department,designation
# salaried - salary, tenure
# casual - rates
class Employee:
    def __init__(self,name:str,id_no:str,department:str,designation:str,gender:str):
        self.name = name
        self.id_no = id_no
        self.department = department
        self.designation = designation
        self.gender = gender
    def print_details(self):
        print(self.name)
        print(self.id_no)
        print(self.department)
        print(self.designation)
        print(self.gender)
        print("**************")
class SalariedEmployee(Employee):
    def __init__(self,name:str,id_no:str,department:str,designation:str,gender:str,salary:float,tenure:float):
        super().__init__(name, id_no, department, designation, gender)
        self.tenure = tenure
        self.salary = salary

class CasualWorker(Employee):
    def __init__(self,name:str,id_no:str,department:str,designation:str,gender:str,rates:float):
        super().__init__(name, id_no, department, designation, gender)
        self.rates = rates
    def calculate_wage(self,hours:float):
        return self.rates * hours


s1 = SalariedEmployee("Samuel James","264678","SHE","Safety Officer","Male",70_000,10)
c1 = CasualWorker("Agnes Daniels","34875432","HR","HR Officer","Female",1500)

s1.print_details()
c1.print_details()
print(c1.calculate_wage(10))