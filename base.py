from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("mensajes")
def open():
    global imagen
    ventana = Toplevel()
    label =Label(ventana,text=" Hola mundo").pack()
    imagen = ImageTk.PhotoImage(Image.open("imagenes/amongus.jfif"))
    label = Label(ventana,image= imagen).pack()

boton = Button(root,text="abrir otra ventana",command=open).pack()
mainloop()