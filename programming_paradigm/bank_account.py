class BankAccount:
    def __init__(self, account_balance: float) -> None:
        if account_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = account_balance
    
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.account_balance += amount
        return True
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self) -> None:
        print(f"Current Balance: ${self.account_balance:.2f}")



