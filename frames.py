from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("frames")

frame = LabelFrame(root,text="frame violento",padx=20,pady=20   )
frame.pack(padx=10,pady=10)
b = Button(frame,text ="no hagas clic")
but= Button(frame,text="no toques")
b.grid(row=0,column=0)
but.grid(row=0,column=1)
root.mainloop()