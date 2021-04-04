from tkinter import *
from tkinter import messagebox
import pyperclip as pc

app = Tk()
app.title("Convert")
app.geometry('700x500+100+100')
app.config(bg="black")

def dec_bin_convert(n):
    if n == '':
        messagebox.showinfo("Wait","Enter Some Decimal Numbers!")
        return
    if not(type(n) == int):
        n = int(n.get())
    if n > 1:
        dec_bin_convert(n//2)
    bin.insert(0, n%2)

def clear():
    dec.delete(0,END)
    bin.delete(0,END)

def copy():
    n = dec.get()
    if n == '':
        messagebox.showinfo("Wait","Enter Some Decimal Numbers!")
        return
    text = "Decimal: "+str((dec.get()))+" \nBinary: "+str(bin.get())
    don = pc.copy(text)
    messagebox.showinfo("Don","Copyed")
    
# title
Label(app,text="Descimal to Binary converter",bg="black",fg="cyan",font=("times bold ", 30)).place(x=100,y=20)


#descimal label
Label(app,text="Decimal Number",bg="black",fg="cyan",font=("times bold ", 15)).place(x=150,y=150)
#decimal entry
dec = Entry(app,bg="black",fg="cyan",font=("times bold ", 30),bd=2,relief=GROOVE,width=20)

#Binary label
Label(app,text="Binary Number",bg="black",fg="cyan",font=("times bold ", 15)).place(x=150,y=300)
#binary entry
bin = Entry(app,bg="black",fg="cyan",font=("times bold ", 30),bd=2,relief=GROOVE,width=20)

Button(app,text="Convert",bg="green",fg="cyan",font=("times bold ", 20),command= lambda x=dec: dec_bin_convert(x),bd=2,relief=GROOVE,width=10).place(x=150,y=430)

Button(app,text="Clear",bg="green",fg="cyan",font=("times bold ", 20),command=clear,bd=2,relief=GROOVE,width=10).place(x=350,y=430)

Button(app,text="Copy",bg="green",fg="cyan",font=("times bold ", 20),command=copy,bd=2,relief=GROOVE,width=5).place(x=550,y=430)

dec.place(x=150,y=180)
bin.place(x=150,y=330)

app.mainloop()
