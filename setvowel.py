str="python language"
list=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', '0', 'U']
c=0

for x in str:
    if x in list:
        c+=1

set={c}

print("No. of vowels: ", set)