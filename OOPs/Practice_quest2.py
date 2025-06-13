"""
Create Account Class with 2 attributes- balance & account no.
Create methods for debit, credit & printing the balance.
"""


class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(50000, 4577)
# print(acc1.balance)
# print(acc1.acc_no)
acc1.debit(10000)
acc1.credit(5000)
