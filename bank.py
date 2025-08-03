class Banking_Sytem:
    def __init__(self,blc,acc):
        self.balance=blc
        self.accountNo=acc
    def credit(self,amount):
        self.balance+=amount
        print("The Amount is Credit",amount)
        print("Total Balance is:",self.get_balance())
    def debit(self,amount):
        self.balance-=amount
        print("The amount was credit",amount)
        print("Total Balance is:",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Banking_Sytem(2300,111122220)
print("Total Balance:",acc1.balance,"Account Number",acc1.accountNo)
acc1.credit(200)
acc1.debit(70)    

print('/n')

acc2=Banking_Sytem(29000,1122331100)
print("Total Balance:",acc2.balance,"Account Number",acc2.accountNo)
acc2.credit(700)
acc2.debit(1800)
acc2.credit(80)
acc2.debit(4500)