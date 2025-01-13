class Checkbook:
    def __inti__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amountt to the balance.
        Parameters:
        amount (float): The amount to deposit. Must ne a positive value.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts the specified amount from the balance if sufficient funds are available.
        Parameters:
        amount (float): The amount to withdraw> must be a positive value.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to run the interactive checkbook program.
    """

    cb = checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be greater than zero. Please try again.")
                else:
                    cd.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be greater than zero. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
