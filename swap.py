a=int(input("Enter a no.:"))
b=int(input("Enter a no.:"))

print("Value before swapping:",a,b)

a=b+a
b=a-b
a=a-b

print("Value after swapping:",a,b)
