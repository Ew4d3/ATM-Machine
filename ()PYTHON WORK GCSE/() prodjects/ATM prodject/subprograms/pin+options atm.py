def pin():
    print("welcome to your accounts")
    print("Please choose an option\n"
          "1)  balances\n"
          "2)  Diposit\n"
          "3)  Withdraw\n"
          "4)  Exit program")
    option=int(input("Which option would you like to run?"))
    if option==1:
        balances()
    if option==2:
        diposit()
    if option==3:
        withdraw()
    if option==4:
                print("signing out")
i=0
def pin():
 while i<3:
        pin_input=("0000")
        print("please insert your card")
        pin=str(input("what is your 4 digit pin?"))
        pinlen=len(pin_input)
        if pin==pin_input:
            print("your pin is correct,welcome")
        if pin!=pinlen:
                print("pin has to be 4 digits")
                i=i+1
        else:
            print("incorrect pin, try again")
        i=i+1
        if i==3:
            print("your card has been blocked, please contact your bank")
