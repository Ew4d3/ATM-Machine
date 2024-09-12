conversion=int(input("what would you like to convert from?\n"
          "  1) Denary to Binary\n"
          "  2) Binary to Denary\n"
          "  3) Letter to Denary\n"
          "  4) Exit\n"
          ))
          
if conversion==1:
    denary()
if conversion==2:
    binary()
if conversion==3:
    letter()
if conversion==4:
    print("Exited")
else:
    print("choose again")

    

def denary():
    binary=int(input("What number would you like to convert to Binary?"))
    if binary==0:
        print("value must be over 0")
        
def binary():
    denary=int(input("What number would you like to convert to Binary?"))
    if denary==0:
        print("value must be over 0")

def letter():
    letter=int(input("What letter woud you like to convert to Denary?"))
    if letter==int:
        print("You must choose a letter")
