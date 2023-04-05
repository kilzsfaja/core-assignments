# *** CODE REVIEW: *** 
# LINE 45, 
# CLASSMETHOD FOR LOOP? (acc in cls.list_of_accounts) - how to work it
# WHATS THE CONNECTION bet. BankAccount and User??

class BankAccount:
    # list_of_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.list_of_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= 5
            print(f"Insuficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}")
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print(f"Sorry, your balance is below 0, cannot process this request!")
        return self

    # @classmethod
    # def print_all_info(cls):
    #     for account in cls.list_of_accounts:
    #         print(f"")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) # CODE REVIEW = WHY IS INT AND BAL DEFINED?
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Account Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Balance: {self.account.balance}")
        return self


lebron_acc = BankAccount(0.1, 100000)
my_acc = BankAccount(0.02, -5)

lebron_acc.deposit(500).deposit(50).deposit(1).withdraw(100000).yield_interest().display_account_info()
my_acc.deposit(500).deposit(500).withdraw(20).withdraw(30).withdraw(10).withdraw(50).yield_interest().display_account_info()

user_saka = User("Bukayo", "starboy.com")
user_saka.make_deposit(100).display_user_balance()

# my_acc.display_account_info()
