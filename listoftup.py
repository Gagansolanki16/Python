list=[2,12,45,88]
list1=[72,42,15,18]
list2=[]

for i in range(len(list)):

    tuple=(list[i],list1[i])

    list2.append(tuple)

print(list2)