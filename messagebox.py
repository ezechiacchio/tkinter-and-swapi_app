from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("mensajes")

def popup():
    #messagebox.showinfo("Este es un mensaje","hiciste algo mal")
    respuesta = messagebox.askokcancel("Este es un mensaje","hiciste algo mal")
    if respuesta== 1:
        Label(root,text="respondiste si").pack()
    else:
        Label(root,text="respondiste no").pack()
    
    

Button(root,text="advertencia",command=popup).pack()


mainloop()