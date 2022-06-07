from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("frames")
root.geometry("600x600")

var = IntVar()
c = Checkbutton(root,text="manzanas",variable=var)
c.pack()
def mostrar():
    label = Label(root,text=var.get()).pack()
    
boton = Button(root,text="mostrar eleccion",command=mostrar).pack()

root.mainloop()