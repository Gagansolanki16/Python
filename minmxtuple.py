list=[(2,11), (55,92), (23,12), (88,8),(11,2)]

max=min=2

for item in list:
    for i in item:
        if i > max:
            max=i

        if i < min:
            min=i
list1=[(min, max)]

print(list1)