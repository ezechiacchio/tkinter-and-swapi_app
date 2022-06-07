from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("programa salvaje")


def abrir():
    global imagen
    root.rutaArchivos = filedialog.askopenfilename(initialdir="eze/pthon/tkinter/imagenes",title="seleccionar imagen",filetypes=(("png","*.png"),("cualquier tipo","*.*")))
    label = Label(root,text = root.rutaArchivos).pack()
    imagen = ImageTk.PhotoImage(Image.open(root.rutaArchivos))
    labelImagen= Label(image=imagen).pack()
    
boton = Button (root,text="abrir archivo",command=abrir).pack()
mainloop()