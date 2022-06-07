import math
from tkinter import *

root = Tk()
root.title("Calculadora")

e= Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    #e.delete(0,END)
    actual=e.get()
    e.delete(0,END)
    e.insert(0, str(actual) + str(number))

def limpiar():
    e.delete(0,END)
    
def sumar():
   primer_numero = e.get()
   global f_num
   global operacion
   operacion="suma"
   f_num= int(primer_numero)
   e.delete(0,END)

def resta():
   primer_numero = e.get()
   global f_num
   global operacion
   operacion="resta"
   f_num= int(primer_numero)
   e.delete(0,END)

def division():
   primer_numero = e.get()
   global f_num
   global operacion
   operacion="division"
   f_num= int(primer_numero)
   e.delete(0,END)

def multiplicacion():
   primer_numero = e.get()
   global f_num
   global operacion
   operacion="multiplicacion"
   f_num= int(primer_numero)
   e.delete(0,END)

def igual():
    segundo_numero=e.get()
    e.delete(0,END)
    if operacion== "suma":
        e.insert(0,f_num + int(segundo_numero))
    elif operacion =="resta":
        e.insert(0,f_num - int(segundo_numero))

    elif operacion == "division":
        e.insert(0,f_num / int(segundo_numero))

    elif operacion == "multiplicacion":
        e.insert(0,f_num * int(segundo_numero))

#definir botones
boton_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
boton_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
boton_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
boton_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
boton_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
boton_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
boton_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
boton_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
boton_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
boton_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
boton_sumar = Button(root,text="+",padx=40,pady=20,command=sumar)
boton_resta = Button(root,text="-",padx=40,pady=20,command=resta)
boton_division = Button(root,text="/",padx=40,pady=20,command=division)
boton_multiplicacion = Button(root,text="X",padx=40,pady=20,command=multiplicacion)
boton_igual = Button(root,text="=",padx=91,pady=20,command=igual)
boton_limpiar = Button(root,text="Clear",padx=79,pady=20,command=limpiar)
#poner los botones en orden
boton_1.grid(row=3,column=0)
boton_2.grid(row=3,column=1)
boton_3.grid(row=3,column=2)

boton_4.grid(row=2,column=0)
boton_5.grid(row=2,column=1)
boton_6.grid(row=2,column=2)

boton_7.grid(row=1,column=0)
boton_8.grid(row=1,column=1)
boton_9.grid(row=1,column=2)

boton_0.grid(row=4,column=0)
boton_sumar.grid(row=5,column=0)
boton_limpiar.grid(row=4,column=1,columnspan=2)
boton_igual.grid(row=5,column=1,columnspan=2)

boton_resta.grid(row=6,column=0)
boton_multiplicacion.grid(row=6,column=1)
boton_division.grid(row=6,column=2)

root.mainloop()