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

                (updated)
