from tkinter import *
top=Tk()
top.geometry("500x500")
top.config(bg="pink")

name=Label(top,text="Name").place(x=30,y=50)
pwd=Label(top,text="pwd").place(x=30,y=90)

e1=Entry(top).place(x=90,y=50)
e2=Entry(top).place(x=90,y=90)

submit=Button(top,text="login").place(x=30,y=120)
top.mainloop()
