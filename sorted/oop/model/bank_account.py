from typing import Self


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmmount, acctName) -> Self:
        self.balance = initialAmmount
        self.name = acctName
        print(f"\bAccount {self.name} created.\nBalance = {self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} balance = ${self.balance:.2f}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("\nDeposite complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n😿 Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete. ✅")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted ❌: {error}")

    def transfer(self, amount, account):
        try:
            print("\n---------------------\n\nBeginning Transfer...💰")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer complete! ✅\n\n---------------------")
        except BalanceException as error:
            print(f"\Transfer interrupted ❌: {error}")


class InterestRewardsAcct(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete. ✅")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmmount, acctName) -> Self:
        super().__init__(initialAmmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWithdraw complete ✅, and Fee is ${self.fee}.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted ❌: {error}")
