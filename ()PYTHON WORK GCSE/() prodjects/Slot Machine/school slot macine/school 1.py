import random
loss=0
winnings=0
money=int(input("how much money would you like to input? £"))
symb=['7','bar','melon','grape','pear','lemon','orange',]
while money>0:
    spin1=random.randint(0,6)
    print("spin 1 is",symb[spin1])
    spin2=random.randint(0,6)
    print("spin 2 is",symb[spin2])
    spin3=random.randint(0,6)
    print("spin 3 is",symb[spin3])
    if spin1 + spin2 + spin3==0:
        print("jackpot!")
        winnings=winnings+1000
        money=money-1
        print("you have won a total of £",winnings)
    if spin1==spin2 or spin1==spin3 or spin2==spin3:
        winnings=winnings+20
        money=money-1
        print("you have won the total of £",winnings)
    if spin1+spin2==2 or spin1+spin3==2 or spin2+spin3==2:
        winnings=winnings+10
        money=money-1
        print("you have won a total of",winnings)
    else:
        print("you have lost")
        loss=loss+1
        money=money-1
        print("you have lost a total of",loss)
print("your total winnings are...£",winnings,"\n"
      "your total lost is...£",loss)


#make differnt fruits have differnt winjings
#make winnings more realistic
