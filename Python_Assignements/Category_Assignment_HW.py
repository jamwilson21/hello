class Category:
    # create the constuctor with parameters:  name and balance 
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        
    # create deposit() method
    def deposit(self , d ):
        self.balance = self.balance + d
    
    # create withdrawal method
    def withdrawal(self , w):
        if(self.balance < w):
            print("You can not complete this transaction. Insufficient Funds.")
        else:
            self.balance = self.balance - w
    # create transfer_fees() method
    def transfer_fees(self):
        self.balance = 30 + self.balance
        
    # create balance_display() method
    def display(self):
        print("Category Name : " , self.name)
        print("Category Balance : " , " $", self.balance)

# different_expenses = Category("Food", 300)
# different_expenses.deposit(1000)
# different_expenses.withdrawal(200)
# different_expenses.transfer_fees()
# different_expenses.display()

# different_expenses = Category("Clothing", 1800)
# different_expenses.deposit(200)
# different_expenses.withdrawal(2900)
# different_expenses.transfer_fees()
# different_expenses.display()

# different_expenses = Category("Car", 0)
# different_expenses.deposit(100)
# different_expenses.withdrawal(10)
# different_expenses.transfer_fees()
# different_expenses.display()