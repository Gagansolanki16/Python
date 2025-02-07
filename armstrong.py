a=int(input("Enter a 3 digit number:"))

no=a
sum=0
rem=0

while a>0:

    rem=a%10
    sum+=rem**3
    a= a//10

if sum==no:
    print(no,"Its a armstrong no.")
else:
    print(no,"Its not an armstrong no.")

