
class Account:
    def __init__(self,password,name,email,address,account_type):
        self.password = password
        self.name = name
        self.address = address
        self.email = email
        self.account_type = account_type
        self.balance = 0
        self.loan_balance = 0
        self.transactions = []
        self.loan_take = 0
    

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited BDT {amount}")
        print("Hello! Your Deposit Successful!!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry!! Your Withdrawal Amount is very High!!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw BDT {amount}")
            print("Your Withdrawal successful!!")

    def check_balance(self):
        print(f"Available balance: BDT {self.balance}")

    def check_transaction_history(self):

        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

            

    def check_loan(self):
        print(f"Your loan balance is {self.loan_balance}.")   


    def take_loan(self,amount):
        if self.loan_take < 2:
            if bank.loan_feature:
                if bank.available_balance() > amount:
                    self.balance += amount
                    self.loan_take -= 1
                    self.loan_balance += amount
                    self.transactions.append(f"You Loan taken BDT {amount}")
                    print("Your Loan taken successfully!!")
                else:
                    print("Sorry!!The bank is bankrupt!")
            else:
                print("Sorry!!Loan feature is currently disabled by admin!")
        else:
            print("Sorry!!You have already taken maximun number of loans!")  


    def return_loan(self,amount):   
        if self.balance >= amount:
            if self.loan_balance > 0 and amount <= self.loan_balance:
                self.balance -= amount
                self.loan_take += 1
                if self.loan_take > 2:
                    self.loan_take = 2
                self.loan_balance -= amount
                self.transactions.append(f"Your Loan returned BDT {amount}")
                print("Your Loan return successfully.")
            elif self.loan_balance > 0 and amount > self.loan_balance:
                self.balance -= self.loan_balance
                self.loan_take += 1
                if self.loan_take > 2:
                    self.loan_take = 2
                self.transactions.append(f"Loan returned BDT {self.loan_balance}")
                self.loan_balance = 0
            elif self.loan_balance <= 0:
                print("You don't have any loan")
        else:
            print("Your Insufficient balance to return loan!!")

    def transfer(self,receiver_number,account_number,amount,bank):
        if receiver_number in bank.users:
            receiver = bank.users[receiver_number]
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transactions.append(f"Transfer BDT {amount} to Account No is : {receiver_number}")
                receiver.transactions.append(f"Transfer BDT {amount} from account {account_number}")
                print("Transfer successful")
            else:
                print("Insufficient balance to transfer.")
        else:
            print("!Receiver account number is invalid!") 

class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan = 0
        self.total_available_balance = 0
        self.loan_feature = True
        self.count = 100

    def create_account(self,password,name,email,address,account_type):
        account = Account(password,name,email,address,account_type)
        account_number = self.count
        self.count += 1
        self.users[account_number] = account
        print(f"Account created successfully!!\n Your account number is {account_number}")

 

    def delete_account(self,account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("Account delete successfully.")
        else:
            print("Account does not exist")

    def show_user(self):
        print("Name\t\tAccounttype\tAccount number")
        for account_number,user in self.users.items():
            print(f"{user.name}\t\t   {user.account_type}\t\t  {account_number}")

    def get_total_balance(self):
        self.total_balance = 0
        for user in self.users.values():
            self.total_balance += user.balance 
        return (self.total_balance)
    def show_total_loan(self):  
        self.total_loan = 0
        for user in self.users.values():
            self.total_loan += user.loan_balance 
        return (self.total_loan)
    def available_balance(self):   
        self.total_available_balance = 0
        self.total_available_balance = self.get_total_balance() - self.show_total_loan()
        return self.total_available_balance
    
    def toggle_loan_feature(self,status):
        self.loan_feature = status
        if status:
            print("Loan feature is enabled.")
        else:
            print("Loan feature is disabled.")



def registration(bank):
    name = input("Enter Your name : ")
    email = input("Enter Your email : ")
    address = input("Enter your address :")
    account_type = "Other"
    print("Choice your account type -")
    print("\t1. Savings ")
    print("\t2. Cuurent ")
    ch = input("\tEnter Your Choice: ") 
    if ch == "1":
        account_type = "Savings"
    elif ch == "2":
        account_type = "Cuurent"
    password = input("Enter Your Password : ")
    bank.create_account(password,name,email,address,account_type)


def user_login(bank):
    account_number = int(input("Enter your account number : "))
    password = input("Enter a password : ")
    if account_number in bank.users:
        if password == bank.users[account_number].password:
            return bank.users[account_number]
        else:
            print("Password is wrong")
            return None
    else:
        print("Invalid account number")
        return None
    
def admin_login():
    username = input("Enter admin username : ")
    password = input("Enter admin password : ")
    if username == "admin" and password == "123":
        return True
    else:
        print("Invalid admin username & password")
        return False
    
bank=Bank()


while True:
    print("\n-----Bank Management System-----")
    print("1. Create User Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")
    ch = input("Enter your choice: ")
    if ch=="1":
        registration(bank)
    elif ch=="2":
        user=user_login(bank)
        if user:
            while True:
                print("\n-----User Menu-----")
                print("1. Transaction->Deposit or Withdraw")
                print("2. Check Balance")
                print("3. Transfer Balance to Another Account")
                print("4. Take Loan")
                print("5. Transaction History")
                print("6. Return Loan")
                print("7. Check Loan Amount")
                print("8. Logout")
                ch = input("Enter your choice : ")
                if ch=="1":
                    print("Enter your transaction type ->")
                    print("\t1. Deposit ")
                    print("\t2. Withdraw ")
                    ch = input("\tEnter your type: ")


                    if ch == "1":
                        amount = int(input("Enter amount to deposit: "))
                        user.deposit(amount)

                    elif ch == "2":
                        amount = int(input("Enter amount to withdraw: "))
                        user.withdraw(amount)
                elif ch == "2":
                    user.check_balance()
                elif ch == "3":
                    receiver_number = int(input("Enter receiver number : "))
                    account_number = int(input("Enter your account number : "))
                    amount = int(input("Enter amount to transfer : "))
                    user.transfer(receiver_number,account_number,amount,bank)

                elif ch == "4":
                    amount = int(input("Enter loan amount : "))
                    user.take_loan(amount)
                elif ch == "5":
                    user.check_transaction_history()
                elif ch == "6":
                    amount = int(input("Enter amount to return loan : "))
                    user.return_loan(amount)
                elif ch == "7":
                    user.check_loan()
                elif ch == "8":
                    break
                else:
                    print("Invalid choice.")
    

    elif ch=="3":
        if admin_login():
            while True:
                print("\n-----Admin Menu-----")
                print("1. Create Account")
                print("2. Delete Account")
                print("3. See All User List")
                print("4. See Total Balance of Bank")
                print("5. See Total Loan")
                print("6. Toggle loan Feature")
                print("7. Logout")

                ch = input("Enter your choice : ")
                if ch == "1":
                    registration(bank)
                elif ch == "2":
                    account_number = (input("Enter account number to delete : "))
                    bank.delete_account(account_number)
                elif ch == "3":
                    print("All user list : ")
                    bank.show_user()
                elif ch == "4":
                    print(f"Total avaliable balance : {bank.available_balance()}")
                    
                elif ch == "5":
                    print(f"Total Loan : {bank.show_total_loan()}")
                    
                elif ch == "6":
                    print("Choice Status ")
                    print("\t1. True ")
                    print("\t2. False ")
                    status = True
                    c = input("\tEnter type: ")
                    if c == "1":
                        status = True
                    elif c == "2":
                        status = False
                    bank.toggle_loan_feature(status)
                elif ch == "7":
                    break
                else:
                    print("Invalid choice.")
    elif ch == "4":
        print("Exit")
    else:
        print("Invalid choice.")

