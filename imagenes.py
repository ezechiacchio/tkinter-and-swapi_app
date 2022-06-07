from tkinter import *
from PIL import ImageTk,Image 
root = Tk()
root.title("imagenes")

img=ImageTk.PhotoImage(Image.open("imagenes/logo.png"))
label = Label(image=img)
label.pack()
boton=Button(root,text="exit_program_",command=root.quit)
boton.pack()
root.mainloop()