from model.bank_account import *

if __name__ == "__main__":
    Lex = BankAccount(1_000_000, "Lex")
    Clark = BankAccount(100, "Clark")

    print(Lex)
    print(Clark)

    Lex.getBalance()
    Clark.getBalance()

    Clark.withdraw(111111)
    Clark.withdraw(10)

    Lex.transfer(1000, Clark)

    Wayne = InterestRewardsAcct(1_200_000, "Wayne")
    Wayne.getBalance()
    Wayne.deposite(1000)

    Barry = SavingsAcct(10000, "Barry")
    Barry.getBalance()
    Barry.transfer(1000, Clark)
