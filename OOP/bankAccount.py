class BankAccount:
    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        if amount < 0:
            print("Insufficiant Funds: Charging a $5 fee")
            self.balance -= 15
        return self

    def display_account_info(self):
        print(f"Balance is ${BankAccount.balance}.")
        return self

    def yield_interest(self):
        pass
        return self

