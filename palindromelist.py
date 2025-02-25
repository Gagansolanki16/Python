list=[121,131,156,234,2,151]

for item in list:
    a=str(item)

    rev=a[::-1]

    if(rev==a):
        print(item)