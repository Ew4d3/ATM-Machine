CA=400             #add write/read text files (new)
SA=400
i=0
def welcome():
    global CA,SA
    print("welcome to your accounts")
    print("Please choose an option\n"
          "1)  Balances\n"
          "2)  Deposit\n"
          "3)  Withdraw\n"
          "4)  Transfer\n"
          "5)  Sign out")
   
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
                print("signed out")
 
def withdraw():     #print ("successfully withdrawed: ", wthdraw)
    global CA,SA
    print("Your balance is..\n"
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
 

       
def deposit():   
   global CA
   print("your current balance is",CA)
   deposit_current=int(input("how much would you like to deposit into current account? £"))
   if deposit_current >=0:
       CA=(CA+deposit_current)
       return CA
       print("your new balance is,\n"
              "£",CA)
      
def transfer():   #print("you have successfully transfered",transfer_current / transfer_savings)
    global CA, SA
    transfer=float(input("Which account would you like to tranfer from?\n"
                         "1)Current account\n"
                         "2)Savings Account\n"
                         "3)Exit\n"
                         ""))
    
    if transfer==1:
        print("your balance is",SA)
        transfer_current=int(input("how much would you like to transfer into your savings account?\n"
                                      "£"))
        if transfer_current>CA:
            print("insoficient funds")
        else:
            CA,SA=(CA-transfer_current , SA+transfer_current)
            return CA,SA
            print("you have successfully transfered", transfer_current)
        
  
    if transfer==2:
        print("your balance is", CA)
        transfer_savings= int(input("how much would you like to transfer into your current account?\n"
                                    "£"))
                                   
        if transfer_savings>SA:
            print("insoficient funds")
        else:
            SA,CA=(SA-transfer_savings , CA+transfer_savings)
            return CA,SA
            print("you have successfully transfered", transfer_savings)
        
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
    pin_input= "0000"
    print("please insert your card")
    pin=str(input("what is your 4 digit pin? "))
    pinlen = len(pin_input)
    if pin==pin_input:
            print("your pin is correct,welcome")
            welcome()
    else:
        print("incorrect pin, try again")
        i=i+1
       
    #fix/write pin len
        
    if i==3:
        print("your card has been blocked, message your bank for futher details")
        
