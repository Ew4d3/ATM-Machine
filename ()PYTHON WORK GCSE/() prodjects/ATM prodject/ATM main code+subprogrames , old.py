CA=200
SA=200
i=0
def welcome():
    print("welcome to your accounts")
    print("Please choose an option\n"
          "1)  balances\n"
          "2)  Diposit\n"
          "3)  Withdraw\n"
          "4)  Exit program")
    option=int(input("Which option would you like to run? "))
    if option==1:
        balances()
    if option==2:
        diposit()
    if option==3:
        withdraw()
    if option==4:
                print("signing out")

def withdraw():  #fix variables and str input
    withdraw_amount=float(input("enter withdrawal amount, £ "))
    if withdraw_amount>CA:
        print("insoficaint funds")
    if withdraw_amount<CA:
        withdraw=(CA-withdraw_amount)
        print("your new balance is,\n"
                  "£",withdraw)
        print("you have withdrawed",withdraw_amount)

def diposit():  #fix whole thing lol
   print("Your Current account balance is:\n"
          "£",CA)
   diposit=float(input("how much would you like to diposit? "))
   if diposit>0:
       CA=(CA+diposit)
       print("your new balance is,\n"
             "£",CA)
       diposit()

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
        if pin!=pinlen:
                print("pin has to be 4 digits")
                i=i+1
        if i==3:
            print("your card has been blocked, please contact your bank")
