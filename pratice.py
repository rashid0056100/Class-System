class Banking_System:
    def __init__(self,bal,name):
        self.balance=bal
        self.name=name

    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"{self.name} deposited {amount}.\n New balance: {self.balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:    
            self.balance-=amount
            print(f"{self.name} withdraw {amount}.\n New balance:{self.balance}")

    def check_balance(self):
        print(f"{self.balance} Your Current Balance:") 

acc1=Banking_System(0,"iqra")
acc1.deposit(133)
acc1.withdraw(100)
acc1.check_balance()

accounts={}
while True:
    print("\n Rashid's Banking System")
    print("\n Choose one")
    print("1.Create Account")
    print("2.User")
    print("3.Quit")
    
    choice=input("Choose one option: ")
    
    if choice == '1':
        name = input("Enter user name: ")
        if name in accounts:
            print("User already exists.")
        else:
            acc = Banking_System(0,name)
            accounts[name] = acc
            print(f"Account created for {name}.")   
    elif choice=="2":
        if name in accounts:
            user=input("Enter user name: ")
            user=accounts[name]
            while True:
                print("Choose One:")
                print("1.Deposit Amount")
                print("2.Withdraw Amount")
                print("3.Check Balance")
                print("4.Back to Main Manu")
                user_choice=input("Choose One option: ")

                if user_choice=="1":
                    amount= float(input("Enter your amount:"))
                    user.deposit(amount)
                elif user_choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif user_choice == '3':
                    user.check_balance()
                elif user_choice == '4':
                    break
                else:
                    print("Invalid option.")
        else:
            print("User Not Found")
    elif choice == '3':
        print("Thanks for using Rashid's Banking System.")
        break

    else:
        print("Invalid Option")
      
