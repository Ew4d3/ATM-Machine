CA=200        #make so variables update from deposit and withdraw CA=(CA-withdraw_amount)etc, test.
SA=200
i=0
def welcome():
    print("welcome to your accounts")
    print("Please choose an option\n"
          "1)  balances\n"
          "2)  Deposit\n"
          "3)  Withdraw\n"
          "4)  Exit program")
    option=int(input("Which option would you like to run? "))
    if option==1:
        balances()
    if option==2:
        deposit()
    if option==3:
        withdraw()
    if option==4:
                print("signing out")

def withdraw():  #add which account would u like to withdraw from...+ only in digits of 5 and 10?(on edge)
    CA=200
    SA=200
    withdraw_amount=float(input("enter withdrawal amount, £ "))
    if withdraw_amount>CA:
        print("insuficient funds")
    if withdraw_amount<CA+1:
        CA=(CA-withdraw_amount)
        print("your new balance is,\n"
                  "£",CA)
        print("you have withdrawed £",withdraw_amount)

def deposit():   #add so u can choose what account to deposit into 
   CA=200
   SA=200
   print("Your Current account balance is:\n"
          "£",CA)
   deposit=int(input("how much would you like to deposit? £"))
   if deposit>0:
       CA_added=(CA+deposit)
       print("your new balance is,\n"
             "£",CA_added)
       
def balances():
    print("Your Current account balance is:\n"
          "£",CA)
    print("your savings account balance is:\n"
          "£",SA)
def pin():  
    i=0
while i<3:
    pin_input=("0000")
    print("please insert your card")
    pin=str(input("what is your 4 digit pin? "))
    pinlen = len(pin_input)
    if pin == pin_input:
        print("your pin is correct,welcome")
        welcome()
        
    else:
        print("incorrect pin, try again")
        i=i+1
        
    #fix this:    
    #if pin!=pinlen:
        #print("pin has to be 4 digits")
                
    if i==3:
        print("your card has been blocked, message your bank for futher details")
