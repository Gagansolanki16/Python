str=str(input("Enter a string:"))

v=c=s=0

for i in str:
    if(i=='A'or i=='a'or i=='I'or i=='i'or i=='E'or i=='e'or i=='O'or i=='o'or i=='U'or i=='u'):
        v=v+1

    elif(i==" "):
        s=s+1
    
    else:
        c=c+1

print("Vowels:",v)
print("Consonant:",c)
print("Space:",s)