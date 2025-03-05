
a=int(input("Enter a year:"))

if(a%4==0 and (a%100!=0 or a%400==0)):
    print(a,"Its a leap year")

else:
    print(a,"It is not a leap year.")

