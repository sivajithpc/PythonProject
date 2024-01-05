class Bank:
    minimum_balance=1000
    balance=0
    account_number = 100000

    def choice_login(self):
        selection=int(input("Enter 1 for account creation, 2 for login, anything else for logout:"))
        if selection==1:
            self.account_creation()
        elif selection==2:
            self.login()
        else:
            print("Logging  out...")
            self.logout()

    def login(self,login_name,password):
        self.login_name=login_name
        self.password=password
        counter_login=0
        while True:
            login_username = str(input("Enter login id:"))
            login_password = str(input("Enter password:"))
            if login_username==self.login_name and login_password==self.password:
                self.choice()
                break
            else:
                if counter_login <= 1:
                    print(f"Username or password is wrong. Try again. {2 - counter_login} attempts remaining.")
                    counter_login+=1
                else:
                    print("Sorry limit reached. Try again after 24 hours")
                    self.blocked()
                    break

    def account_creation(self):
        first_name=str(input("Enter your first name:"))
        last_name=str(input("Enter your last name:"))
        login_name=str(input("Create login id:"))
        counter=0
        while True:
            password = str(input("Set your password:"))
            re_password = str(input("Confirm your password:"))
            if password == re_password:
                global account_number
                self.account_number+=1
                print("Password matched")
                print(f"Dear {first_name} {last_name} ,your account has been created successfully. Account number is {self.account_number}")
                self.login(login_name, password)
                break
            else:
                if counter <= 1:
                    print(f"Password not matching. Try again. {2-counter} attempts remaining.")
                    counter += 1
                else:
                    print("Sorry limit reached. Try again.")
                    self.logout()
                    break

    def choice(self):
        selection=int(input("Enter 1 for deposit, 2 for withdrawal, anything else for logout:"))

        if selection==1:
            self.deposit()
        elif selection==2:
            self.withdraw()
        else:
            print("Logging out...")
            self.logout()

    def deposit(self):
        print(f"Your current balance is ₹{self.minimum_balance}")
        deposit_amount=float(input("Enter the amount to be deposited (₹):"))
        if deposit_amount>=0:
            print(f"Deposited ₹{deposit_amount}")
            self.balance = self.minimum_balance + deposit_amount
            print(f"Your current balance is ₹{self.balance}")
        else:
            print("Invalid amount")
            self.logout()



    def withdraw(self):
        print(f"Your current balance is ₹{self.balance}")
        withdraw_amount=float(input("Enter the amount to be withdrawn (₹):"))
        if withdraw_amount>=0:
            if (self.balance - withdraw_amount) < 1000:
                print("Your balance is too low. Try another amount.")
                self.withdraw()
            else:
                self.balance = self.balance - withdraw_amount
                print(f"Withdrawn ₹{withdraw_amount}")
                print(f"Your current balance is ₹{self.balance}")
        else:
            print("Invalid amount")
            self.logout()

    def logout(self):
        print("You are logged out.")

    def blocked(self):
        print("Your account has been blocked for 24 hours.")

b=Bank()
b.choice_login()
b.withdraw()
