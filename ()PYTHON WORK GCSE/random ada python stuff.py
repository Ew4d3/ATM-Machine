pin = "1234"
def  menu():
    global pin
    pinInput = int(input("What is your password? "))
    pinLength = pinInput
    pinLen =  len(pinLength)
    if pinLen == 4:
        if pinInput == pin:
            print("well done you have access!")
        else:
            print("Wrong password")
    else:
        print("your pin is longer than 4 digits")
            
menu()
