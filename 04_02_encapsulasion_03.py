class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdrawal amount must be positive and not exceed the balance.")

    @property
    def balance(self):
        return self.__balance

# Membuat objek
account = BankAccount(1000)

# Menggunakan metode untuk mengakses dan mengubah saldo
account.deposit(500)
print(account.balance)  # Output: 1500

account.withdraw(300)
print(account.balance)  # Output: 1200
