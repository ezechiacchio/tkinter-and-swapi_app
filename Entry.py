from tkinter import *

root = Tk()
e= Entry(root)
e.pack( )
e.insert(0,"ingrese su nombre")
def myClick():
    hello= "hola " + e.get()
    mylabel = Label(root,text=hello)
    mylabel.pack()

mybutton = Button(root,text="aceptar    ",padx=150,command=myClick,fg="blue",bg="red")

mybutton.pack()
root.mainloop()