str=str(input("Enter a string:"))

if(len(str)<2):
    print("The string is empty.")

else:
    str1=str[0:2]+str[-2:]
    print(str1)