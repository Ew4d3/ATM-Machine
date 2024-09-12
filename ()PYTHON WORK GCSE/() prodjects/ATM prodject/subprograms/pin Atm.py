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


            (updated)
