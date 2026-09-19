

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")


if __name__ == "__main__":
    account = BankAccount("Tendai", 100)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(1000)  # should fail, insufficient funds
    account.display_balance()

    # Direct access is blocked because __balance is private:
    # account.__balance = 999999  # this would NOT work as expected
    # print(account.__balance)    # this raises an AttributeError
