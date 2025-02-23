list1=[35,23,56,76,29]
list2=[15,43,50,86,9]

list3=[]
c=0

for i in list1:
    j=list2[c]
    a=i-j

    if(a>0):
        list3.append(i)
    c+=1

print(list3)