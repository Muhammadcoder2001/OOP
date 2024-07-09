'''
4. Account nomli klass yarating. Unda quyidagi rasmda ko'rsatilgan atribut va metodlarni yarating.
Account
-id:String
-name:String
-balance:int = 0

+Account(id:String,name:String)
+Account(id:String,name:String,balance:int)
+getId():String
+getName():String
+getBalance():int
+credit(amount:int):int
+debit(amount:int):int
+transferTo(another:Account, amount:int):int
+toString():String

Add amount to balance, return balance

If amount <= balance
  subtract amount from balance
else print "Amount exceeded balance"
return balance

If amount <= balance
  transfer amount to the given Account
else print "Amount exceeded balance"
return balance

"Account[id=?,name=?,balance=?]"
'''

class Account:
    def __init__(self, ID, name, balance):
        self.ID = ID
        self.name = name
        self.balance = balance

    def short_data(self):
        # self.ID = ID
        # self.name = name
        return f"Id: {self.ID} Name: {self.name}"
    
    def get_info(self):
        return f"Id: {self.ID} Name: {self.name} Balance: {self.balance}$"
    

    def get_id(self):
        return f"Id :{self.ID}"

    def get_name(self):
        return f"Name: {self.name}"
    
    def get_balance(self):
        return f"Balance: {self.balance}$"
    
    def see_credit(self, credit:int)-> int:
        return f"{self.balance + credit}$"
    

    def see_debit(self, debit:int)->int:
        if debit > self.balance:
            return f"Amount exceeded balance: {self.balance}$"
        else:
            return f"Subtracting process is Done {self.balance - debit}$"
        
    def transfer_balance(self, transfer_summa:int)->int:
        if transfer_summa < self.balance:
            return f"{self.balance - transfer_summa}$"
        else:
            return f"Your balance less than transfer balance!!! {self.balance}$"

class Another:
    def __init__(self, balance):
        self.balance = balance       

user =Account("432qwerty", "Anvar", 12000)
# print(user.get_info())
# print(user.short_data())
# print(user.get_id())
# print(user.credit(1000))
# print(user.see_debit(1300))
user2 = Another(3500)
print(user.transfer_balance(user2.balance))





