#def deposit():  #add so u can choose what account to deposit into 
   CA=200
   SA=200
   print("Your Current account balance is:\n"
          "£",CA)
   deposit=int(input("how much would you like to deposit? £"))
   if deposit>0:
       CA_added=(CA+deposit)
       print("your new balance is,\n"
             "£",CA_added)

#(updated)
