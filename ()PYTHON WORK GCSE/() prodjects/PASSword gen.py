import random
import string
pword1=input("input a passord")
if len (pword1)<8:
   print("weak password")
if pword1[-1]=="!"or"?":
   print("good password")
   choice=input("would you like a stronger password?")
   if choice=="yes":
      i=0
      while i<8:
         randomletter = random.choice(string.ascii_letters)
         password=(randomletter)
         i=i+1
         print(randomletter)
   
      print(password)
