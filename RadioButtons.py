from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("botones redondos")

def seleccion(valor):
    label= Label(root,text=valor)
    label.pack()    
#r = IntVar()
#r.set("2")
#Radiobutton(root,text="manzana",variable=r,value=1,command=lambda:seleccion(r.get())).pack()
#Radiobutton(root,text="pera",variable=r,value=2,command=lambda:seleccion(r.get())).pack()
tuplas=[
    ("pepperoni","pepperoni"),
    ("napolitana","napolitana"),
    ("muzza","muzza"),
    ("jamon","jamon"),
]
pizza = StringVar()
pizza.set("pepperoni")

for text,tupla in tuplas:
    Radiobutton(root,text=text,variable=pizza,value=tupla).pack()
boton = Button(root,text="pedir pizza",command=lambda:seleccion(pizza.get()))
label= Label(root,text=pizza.get())
label.pack()
boton.pack()
root.mainloop()
