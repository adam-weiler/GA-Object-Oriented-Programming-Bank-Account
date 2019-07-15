class BankAccount: #A bank account class.
    def __init__(self, balance, interest_rate): #Every bank account has instance variables balance, and interest_rate.
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self): #Returns a meaningful string that describes the instance.
        return (f'The current bank account has a balance of ${self.balance} at an interest rate of {self.interest_rate}%.')

    def deposit(self, amount): #An instance method adds the amount to the instance's balance.
        self.balance += amount

    def withdraw(self, amount): #An instance method subtracts the amount from the instance's balance.
        self.balance -= amount

    def gain_interest(self): #An instance method calculates interest and adds the amount to the instance's balance.
        self.balance += round((self.balance * self.interest_rate),2)


first_account = BankAccount(50, .014) #Creates an instance of the BankAccount class.
first_account.deposit(25) #Calls the deposit instance method.
first_account.withdraw(8.5) #Calls the withdraw instance method.
first_account.gain_interest() #Calls the gain_interest instance method.
print(first_account) #Prints the meaningful string after the calculations are complete.
print()

second_account = BankAccount(1000, .018) #Creates another instance of the BankAccount class.
second_account.deposit(500) #Calls the deposit instance method.
second_account.withdraw(680) #Calls the withdraw instance method.
second_account.gain_interest() #Calls the gain_interest instance method.
print(second_account) #Prints the meaningful string after the calculations are complete.
print()

third_account = BankAccount(2000, .02) #Creates another instance of the BankAccount class.
third_account.deposit(800) #Calls the deposit instance method.
third_account.withdraw(750) #Calls the withdraw instance method.
third_account.gain_interest() #Calls the gain_interest instance method.
print(third_account) #Prints the meaningful string after the calculations are complete.
print()

print (third_account.__dict__) #Dictionary containing the class's namespace: {'balance': 2091.0, 'interest_rate': 0.02}
print (third_account.__doc__) #Class documentation string: None
# print (third_account.__name__) #Class name: There is no attribute __name__
print (third_account.__module__) #Module name in which the class is defined: __main__
# print (third_account.__bases__) #A possibly empty tuple containing the base classes, in the order of their occurance in the base class list: There is no attribute __bases__