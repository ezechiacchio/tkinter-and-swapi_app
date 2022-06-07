from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("programa salvaje")
root.geometry("400x400")
def deslizar(cantidad):
    label = Label(root,text=horizontal.get()).pack()
    root.geometry(str(cantidad)+"x"+str(vertical.get()))

vertical= Scale(root,from_ = 300 , to=1000)
vertical.pack()
horizontal = Scale(root,from_ = 500 , to=1000,orient=HORIZONTAL,command=deslizar)
horizontal.pack()

boton = Button(root,text="cambiar relacion",command=deslizar).pack()
mainloop()