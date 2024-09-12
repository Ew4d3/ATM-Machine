CA=200
SA=200
i=0
def welcome():
    global CA,SA
    print("welcome to your accounts")
    print("Please choose an option\n"
          "1)  balances\n"
          "2)  Deposit\n"
          "3)  Withdraw\n"
          "4)  Transfer\n"
          "5)  Exit program")
    
    option=int(input("Which option would you like to run? "))
    if option==1:
        balances()
    if option==2:
        deposit()
    if option==3:
        withdraw()
    if option==4:
        transfer()
    if option==5:
                print("signing out...")

def withdraw(): 
    global CA
    print("Your current balance is:\n"
                  "£",CA)
    Withdraw=float(input("How much do you want to withdraw? £"))
    multiple=(Withdraw%10)
    if multiple==0:
        if Withdraw >=10 and Withdraw <=250:
            CA=(CA-Withdraw)
            return CA
            print("Your new balance is £ ", CA)
        else:
            print("You can only withdraw a minimum of £10 and maximum of £250")
    else:
        print("make sure the amount you inputed is a multiple of 10")


def deposit():   #choose what account to deposit into
   global CA,SA
   print("Your Current account balance is:\n"
          "£",CA)
   deposit_account=int(input("Which account would you like to deposit into?\n"
         "1)  current account\n"
         "2)  Savings account\n"
         "3)  Exit\n"
         ""))
   if deposit_account==1:
       deposit=int(input("how much would you like to deposit into current account? £"))
       CA=(CA+deposit)
       return CA
       print("your new balance is,\n"
              "£",CA)
       welcome()
       
   elif deposit_account==2:
       deposit=int(input("how much would you like to deposit into savings account? £"))
       SA=(SA+deposit)
       return SA
       print("your new balance is,\n"
             "£",SA)
   if deposit_account==3:
       print("exiting program")
       

def transfer():  #fix 
    global CA,SA
    transfer=float(input("Which account would you like to tranfer from?\n"
                         "1)Current account\n"
                         "2)Savings Account\n"
                         "3)Exit\n"
                         ""))
    if transfer==1:
        transfer_current=int(input("how much would you like to transfer into your savings account?\n"
                                      "£"))
        if transfer_current>CA:
            print("insoficient funds")
        CA,SA=(CA-transfer_current , SA+transfer_current)
        return CA,SA
    print("you have transfered", transfer_current)
        
    if transfer==2:
        transfer_savings=int(input("how much would you like to transfer into your current account?\n"
                                      "£"))
        if transfer_savings>CA:
            print("insoficient funds")
        SA,CA=(SA-transfer_savings , CA+transfer_savings)
        return SA,CA
    
    else:
        print("make sure you have chosen the correct account/s")
        
        
    
def balances():
    global CA,SA
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
        
    #fix pin len 
        
    #if pin!=pinlen:
                #print("pin has to be 4 digits")
                
    if i==3:
        print("your card has been blocked, message your bank for futher details")
