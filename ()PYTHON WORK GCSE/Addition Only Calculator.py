num1=int(input("what is your first number ?"))
num2=int(input("what is your second numer?"))
meth=input("what is your chosen method?~(write the symbol for example multiplication is x):\n")
if meth=='x':
    end1=(num1*num2)
    print (end1)
if meth=='+':
    end2=(num1+num2)
    print (end2)
if meth=='/':
    end3=(num1/num2)
    print (end3)
if meth=='-':
    end4=(num1-num2)
    print (end4)
if meth=='2':
    end5=(num1*num1+num2*num2)
    print (end5)
