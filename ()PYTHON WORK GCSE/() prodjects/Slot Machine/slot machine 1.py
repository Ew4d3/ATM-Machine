import random
#1=apple,2=pear,3=bannana,4=pineapple,5=peach,6=kiwi.7=lime.8=orange,9=grape,10=gold
def start():
   balance=0
   if balance<1:
      balance=int(input("how mucb would you like to deposit?\n"
               "£"))
   if balance>=1:
      bet=int(input("how much would you like to bet?\n"
            "£"))
   if balance<bet:
      print("you do not have enough funds,please deposit more or exit")
      start()
   if balance>=bet:
      spin()

def cash():
   c=int(input("would you like to cash out?\n"
               "1=yes\n"
               "2=no\n"))
   if c==1:
      print("money has been cashed out")
   if c==2:
      spin()
def spin():
   ready=int(input("are you ready to play?\n"
         "1=yes\n"
         "2=no\n"))
   if ready==1:
      print("ok spinning........")
      numbers()
      
def numbers():
         number1=random.randint(1,10)
         if number1==10:
            print("Win! Your number was 10!")
            cash()
         else:
            print("your first number is",number1)
         number2=random.randint(1,10)
         if number2==10:
            print("Win! Your number was 10!")
            cash()
         else:
            print("your second number is",number2)
         number3=random.randint(1,10)
         if number3==10:
            print("Win! Your number was 10!")
            cash()
         else:
            print("your third number is",number3)
            spin()
         if number1==number2 and number1==number3:
            print("Triple Win!")
            win=number1+number2+number3*3
            print(win)
            cash()
       
start()
#random=random.randint(1,5)
#print(random)

