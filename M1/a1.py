#REFERENCE: https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/


class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError("Account is Empty, No money!")
        self.balance -= amount

    def get_balance(self):

        return self.balance


def main():
    customer1 = BankAccount('Vishal')
    print(customer1.name)
    print(customer1.get_balance())
    customer1.deposit(1000)
    customer1.withdraw(485)
    print(customer1.get_balance())



if __name__ == "__main__":
    main()
        