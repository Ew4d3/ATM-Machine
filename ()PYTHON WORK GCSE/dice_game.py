import random
print("The aim of the game is to guess the total of the two dice!")
numb1=random.randint(1,6)
numb2=random.randint(1,6)
total=int(numb1+numb2)
guess=int(input("What is your guess? "))
if guess == total:
    print("Correct guess!")
else:
    print("Wrong! Try again next time!")
    print("The total was: ", total)
    

