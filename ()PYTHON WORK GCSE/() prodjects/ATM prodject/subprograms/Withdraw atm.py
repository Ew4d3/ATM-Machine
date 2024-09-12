def withdraw():  #add which accont would u like to withdraw from...+ only in digits of 10?
    CA=200
    SA=200
    withdraw_amount=float(input("enter withdrawal amount, £ "))
    if withdraw_amount>CA:
        print("insuficient funds")
    if withdraw_amount<CA:
        CA=(CA-withdraw_amount)
        print("your new balance is,\n"
                  "£",CA)
        print("you have withdrawed",withdraw_amount)

        (updated)

