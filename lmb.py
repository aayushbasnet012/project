from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("REg/Log")

def click():
    root1 = Tk()
    root1.geometry("300x300")
    root1.title("Log In")
    l1=Label(root1,text="Username").pack()
    entr1y=Entry(root1).pack()
    l2=Label(root1,text="Password").pack()
    entry2=Entry(root1)
    entry2.config(show="*")
    entry2.pack()

def reg():
    root1 = Tk()
    root1.geometry("300x300")
    root1.title("Register")
    l1=Label(root1,text="Username").pack()
    entry=Entry(root1).pack()
    l2=Label(root1,text="Password").pack()
    entry2=Entry(root1)
    entry2.config(show="*")
    entry2.pack()
    
    
button1= Button(root,text="LOG IN",command=click)
button1.pack()
button2= Button(root,text="REGISTER",command=reg)
button2.pack()

root.mainloop()


