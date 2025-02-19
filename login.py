from tkinter import*
root=Tk()
root.title("Login page")
root.geometry("300x300")


lbl= Label(root,bd=5,text="Username:")
lbl.grid(row=0,column=0)
ent1= Entry(root,bd=5)
ent1.grid(row=0,column=1)


lbl2= Label(root,bd=5,text="Password:")
lbl2.grid(row=1,column=0)
ent2= Entry(root,bd=5)
ent2.grid(row=1,column=1)

login=Button(root,bd=5,text="Login",relief="groove")
login.grid(row=5,column=0,padx=25,pady=5)

reg=Button(root,text="Register",bd=5,relief="groove")
reg.grid(row=5,column=1,padx=0,pady=5)
root.mainloop()