from tkinter import *
from PIL import ImageTk,Image 
root = Tk()
root.title("imagenes")

imagen1=ImageTk.PhotoImage(Image.open("imagenes/amongus.jfif"))
imagen2=ImageTk.PhotoImage(Image.open("imagenes/juego.jfif"))
imagen3=ImageTk.PhotoImage(Image.open("imagenes/logo.png"))
imagen4=ImageTk.PhotoImage(Image.open("imagenes/minecraft.jfif"))
lista_imagenes=[imagen1,imagen2,imagen3,imagen4]

milabel = Label(image=imagen1)
milabel.grid(row=0,column=0,columnspan=3)

def adelante(num_imagen):
    global milabel
    global boton_siguiente
    global boton_anterior
    numero_imagen=num_imagen
    milabel.grid_forget()
    milabel=Label(image=lista_imagenes[num_imagen])
    boton_siguiente=Button(root,text=">>",command=lambda:adelante(numero_imagen+1))
    boton_anterior=Button(root,text="<<",command=lambda:atras(numero_imagen-1))
    
    milabel.grid(row=0,column=0,columnspan=3)
    boton_anterior.grid(row=1,column=0)
    boton_adelante.grid(row=1,column=2)

def atras():
    return
boton_anterior= Button(root, text="<<",command=lambda:atras())
boton_salir=Button(root,text="Salir",command=root.quit)
boton_adelante=Button(root,text=">>",command=lambda:adelante(2))
boton_anterior.grid(row=1,column=0)
boton_adelante.grid(row=1,column=2)
boton_salir.grid(row=1,column=1)
root.mainloop()