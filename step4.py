# 4. Class Variables and Class Methods

# Assignment:

# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "Old Bank Name"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")


# Creating instances of Bank
customer1 = Bank("Alice")
customer2 = Bank("Bob")

# Display initial info
print("Before changing bank name:")
customer1.display_info()
customer2.display_info()

# Changing the bank name using class method
Bank.change_bank_name("New Generation Bank")

# Display info after changing the bank name
print("\nAfter changing bank name:")
customer1.display_info()
customer2.display_info()
