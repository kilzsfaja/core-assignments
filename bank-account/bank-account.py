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
        return self

    # @classmethod
    # def print_all_info(cls):
    #     for account in cls.list_of_accounts:
    #         print(f"")

lebron_acc = BankAccount(0.1, 100000)
my_acc = BankAccount(0.02, 1)

lebron_acc.deposit(500).deposit(50).deposit(1).withdraw(100000).yield_interest().display_account_info()

my_acc.deposit(500).deposit(500).withdraw(20).withdraw(30).withdraw(10).withdraw(50).yield_interest().display_account_info()

# my_acc.display_account_info()