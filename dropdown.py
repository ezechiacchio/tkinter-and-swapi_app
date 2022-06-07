from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("frames")
root.geometry("600x600")

def mostrar():
    label = Label(root, text=var.get()).pack()

opciones = [
    "Lunes",
    "Martes",
    "miercoles",
    "jueves",
    "viernes"
]


var = StringVar()
var.set(opciones[0])
drop = OptionMenu(root, var,*opciones)
drop.pack()
boton = Button(root,text="Mostrar eleccion", command=mostrar).pack()
root.mainloop()