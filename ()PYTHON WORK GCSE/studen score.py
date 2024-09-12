i=0
total=0
highest=0
lowest=0
while i < 10 :
    num=int(input("what is the students score"))
    if num<10:
        i=i+1
        total=(total+num)
    else:
        print("over 10")
print("total score is",total)
average=(total/10)
print("your average score is",average)
if num<lowest:
    lowest=(num)
    print("the lowest is",lowest)
