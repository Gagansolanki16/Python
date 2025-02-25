a= float(input("Enter a number:"))
b= float(input("Enter a number:"))

try:
    print(a/b)

except ZeroDivisionError:
    print("Division by 0.")

except ArithmeticError:
    print("An arithmetic error.")

except:
    print("Error.")
