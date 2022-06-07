from tkinter import *

root = Tk()
def myClick():
    mylabel = Label(root,text="Look. I Clicked the button")
    mylabel.pack()

mybutton = Button(root,text="click me",padx=150,command=myClick,fg="blue",bg="red")

mybutton.pack()
root.mainloop()