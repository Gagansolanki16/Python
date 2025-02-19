from tkinter import*
root=Tk()
root.title("Registration Form")
root.geometry("600x500")


lbl= Label(root,bd=5,text="Username:")
lbl.grid(row=0,column=0)
ent1= Entry(root,bd=5)
ent1.grid(row=0,column=1)

lbl1= Label(root,bd=5,text="Age:")
lbl1.grid(row=1,column=0)
ent2= Entry(root,bd=5)
ent2.grid(row=1,column=1)

var=IntVar()
lbl2= Label(root,bd=5,text="Gender:")
lbl2.grid(row=2,column=0)
rb=Radiobutton(root,text="Male",variable=var,value=1)
rb.grid(row=2,column=1)

rb1=Radiobutton(root,text="Female",variable=var,value=2)
rb1.grid(row=2,column=2)

lbl3= Label(root,bd=5,text="Email:")
lbl3.grid(row=3,column=0)
ent3= Entry(root,bd=5)
ent3.grid(row=3,column=1)

lbl4=Label(root,text="College:")
lbl4.grid(row=4,column=0)
menu=StringVar()
menu.set("Select your college:")

check= Checkbutton(root,text="I hereby confirm that all this information provided by me is correct.")
check.grid(row=5,column=1)
drop= OptionMenu(root,menu,"MSU","SVIT","GTU","LD")
drop.grid(row=4,column=1)

btn=Button(root,text="Submit")
btn.grid(row=6,column=1)


# btn1=Button(root,text="Cancel")
# btn1.grid(row=7,column=1)
root.mainloop()