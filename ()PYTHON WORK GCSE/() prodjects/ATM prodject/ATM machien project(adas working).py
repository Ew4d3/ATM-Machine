CurrentBalance=200
SavingsAccount=500
loop=1
def balance():
    global CurrentBalance
    print("Your balance is...\n"
                  "£", CurrentBalance)
def withdraw():
    global CurrentBalance
    print("Your balance is...\n"
                  "£", CurrentBalance)
    Withdraw=float(input("How much do you want to withdraw?"))
    multiple=(Withdraw%10)
    if multiple==0:
        if Withdraw >=10 and Withdraw <=250:
            CurrentBalance=(CurrentBalance-Withdraw)
            return CurrentBalance
            print("Your new balance is £ ", CurrentBalance)
            loop=0
            main_screen()
        else:
            print("You can only withdraw a minimum of £10 and maximum of £250")
            loop=0
    else:
        print("make sure the amount you inputed is a multiple of 10")
def deposit():
    global CurrentBalance
    global SavingsAccount
    Deposit=float(input("What account do you want to deposit into?\n"
                        ""
                        "1) Savings account\n"
                        "2) Current account\n"
                        ""
                        "Please enter the account you want to deposit into: "))
    if Deposit==1:
        Deposit_calculation=int(input("How much money do you want to deposit into this account: £"))
        SavingsAccount=(SavingsAccount+Deposit_calculation)
        return SavingsAccount
        print("Your new balance is £ ", SavingsAccount)
        loop=0
        main_screen()
    elif Deposit==2:
        Deposit_calculation=int(input("How much money do you want to deposit into this account: £"))
        CurrentBalance=(CurrentBalance+Deposit_calculation)
        return CurrentBalance
        print("Your new balance is £ ", CurrentBalance)
        loop=0
        main_screen()
    else:
        print("No deposit made, make sure you entered the number according to the account you want to deposit into!")

def transfer():
    global CurrentBalance, SavingsAccount
    print("What account do you want to transfer from?\n "
                         "1) Current Account\n"
                         "2) Savings Account\n"
                         "3) Exit\n"
                         "Please pick one of the NUMBERS given")
    transfer=float(input("Pick a number: "))
    if transfer==1:
            transfer1=float(input("How much money do you want to transfer into your savings account? £ "))
            if CurrentBalance<=transfer1:
                CurrentBalance=(CurrentBalance-transfer1)
                return CurrentBalance
                SavingsAccount=(SavingsAccount+transfer1)
                return SavingsAccount
            else:
                print("Make sure you have enough funds in your account")
    elif transfer==2:
        transfer2=float(input("How much money do you want to transfer into your current account? £ "))
        if CurrentBalance<=transfer2:
            SavingsAccount=(SavingsAccount-transfer2)
            return SavingsAccount
            CurrentBalance=(CurrentBalance+transfer2)
            return CurrentBalance
        else:
            print("Make sure you have enough funds in your account")
    elif transfer==3:
        print("Ok exiting the program right now", exit())
    else:
        print("not working")
        
            
while loop == 1:
    def main_screen():
        print(" Welcome to my ATM ")
        print("Select your option\n"
              "1)    Balance\n"
              "2)    Withdraw\n"
              "3)    Deposit\n"
              "4)    Transfer\n"
              "5)    Exit\n"

              "")
        Option=int(input("What number do you choose: "))
        if Option==1:
            balance()
        if Option==2:
            withdraw()
        if Option==3:
            deposit()
        if Option==4:
            transfer()
        if Option==5:
            loop=0
            exit()
            

    PIN=1234
    i=0
    while i < 3:
        print("Please enter your card... ")
        PINinput=int(input("Please enter your 4-digit PIN: "))
        if PINinput == PIN:
            main_screen()
        else:
            print("try again")
            i=i+1
            loop=0
            if i == 3:
                print("Your card has been blocked, please contact your bank")
       
