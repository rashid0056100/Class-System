import json
import os

class Banking_System:
    def __init__(self, bal, name, password):
        self.balance = bal
        self.name = name
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited {amount}.\nNew balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}.\nNew balance: {self.balance}")

    def check_balance(self):
        print(f"{self.name}, your current balance is: {self.balance}")

def save_accounts():
    data = {
        name: {
            "balance": acc.balance,
            "password": acc.password
        } for name, acc in accounts.items()
    }
    with open("users.json", "w") as f:
        json.dump(data, f)

def load_accounts():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            try:
                data = json.load(f)
                for name, info in data.items():
                    if isinstance(info, dict) and "balance" in info and "password" in info:
                        accounts[name] = Banking_System(info["balance"], name, info["password"])
                    else:
                        print(f"⚠️ Skipping corrupted user data for: {name}")
            except json.JSONDecodeError:
                print("⚠️ users.json is corrupted or empty. Starting fresh.")

accounts = {}
load_accounts()

while True:
    print("\n--- Rashid's Banking System ---")
    print("1. Create Account")
    print("2. User Login")
    print("3. Quit")

    choice = input("Choose one option: ")

    if choice == '1':
        name = input("Enter username: ")
        if name in accounts:
            print("⚠️ User already exists.")
        else:
            password = input("Set your password: ")
            acc = Banking_System(0, name, password)
            accounts[name] = acc
            save_accounts()
            print(f"✅ Account created for {name}.")

    elif choice == '2':
        name = input("Enter username: ")
        if name not in accounts:
            print("❌ User not found.")
        else:
            password = input("Enter password: ")
            if accounts[name].password != password:
                print("❌ Incorrect password.")
            else:
                user = accounts[name]
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit Amount")
                    print("2. Withdraw Amount")
                    print("3. Check Balance")
                    print("4. Back to Main Menu")
                    user_choice = input("Choose one option: ")

                    if user_choice == '1':
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            user.deposit(amount)
                            save_accounts()
                        except ValueError:
                            print("⚠️ Invalid input. Enter a number.")
                    elif user_choice == '2':
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            user.withdraw(amount)
                            save_accounts()
                        except ValueError:
                            print("⚠️ Invalid input. Enter a number.")
                    elif user_choice == '3':
                        user.check_balance()
                    elif user_choice == '4':
                        break
                    else:
                        print("Invalid option.")

    elif choice == '3':
        print("👋 Thanks for using Rashid's Banking System.")
        break

    else:
        print("❌ Invalid option.")
