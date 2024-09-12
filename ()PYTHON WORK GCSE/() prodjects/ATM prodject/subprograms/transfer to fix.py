CA=200
SA=200

global CA,SA
transfer=float(input("What account would you like to transfer from?\n"
                               "1)  Current account,\n"
                               "2)  Savings account,\n"
                               "3)  Exit\n"
                                   ""))
if transfer==1:
        transfer_total=int(input("how much would you like to transfer to Savings account?  £"))
if transfer_total>CA:
                print("insuficient funds")
    transfer_total=(CA-transfer_total , SA+transfer_total)
return CA,SA

if transfer==2:
        transfer_total2=int(input("how much would you like to transfer to current account?  £"))
if transfer_total2>SA:
                print("insuficient funds")
    transfer_total2=(SA-transfer_total2 , CA+transfer_total2)
    return CA,SA
            
