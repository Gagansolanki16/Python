# import math

# a= int(input("Enter a number:"))
# b= int(input("Enter a number:"))

# c=math.pow(a,b)
# print(c)

a= int(input("Enter a number:"))
b= int(input("Enter a number:"))

def power(a,b):
    n=a

    for i in range(1,b):
        a=a*n

    return a

res=power(a,b)
print(res)