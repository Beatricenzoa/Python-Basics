# classes
# customer - names, email, kra_pin,dob,gender
# BankAccount - customer, acc_no, acc_type, balance
class Customer:
    def __init__(self, names:str, email:str,kra_pin:str,dob:str,gender:str):
        self.names = names
        self.email = email
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender
    def show_details(self):
        print(f"Name : {self.names} and KRA Pin : {self.kra_pin}")
    def __str__(self) :
        return f"{self.names}"

class Account:
    def __init__(self,owner:Customer,acc_no:str,acc_type:str,balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.acc_type)
        print(self.balance)
        print("--------------")

    def deposit(self,amount:float):
        self.balance += abs(amount) # abs makes a negative amount positive

    def withdraw(self,amount:float):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= abs(amount)
    def __str__(self):
        return f"This account belongs to {self.owner.names} and is a {self.acc_type} account"
owner1 = Customer("Noel Michael","noel@test.com","KRA123","20-01-1990", "Male")
owner2= Customer("Mary Mark","mary@test.com","KRA125","10-05-2001", "Female")

acc1 = Account(owner1,"1467892567","current",5_000)
acc2 = Account(owner1,"1467892570","savings",1_000_000)
acc3 = Account(owner2,"1467892580","savings",100_000)

acc1.print_details()
acc1.deposit(10_000)
acc1.print_details()
acc1.withdraw(2_000)
acc1.print_details()

print(acc1.owner)
print(acc1)