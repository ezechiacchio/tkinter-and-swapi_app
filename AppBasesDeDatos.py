from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN
from PIL import ImageTk,Image
import sqlite3

from setuptools import Command

root=Tk()
root.title("UsuariosApp")
root.geometry("500x500")


#crear tabla
#c.execute("""CREATE TABLE direcciones (
#    nombre text,
#    apellido text,
#    calle text,
#    ciudad text,
#    provincia text,
#    codigo_postal integer
#)""")
#crear funcion submit
def submit():

    #crear o conectar una base de datos
    conn = sqlite3.connect('address_book.db')

    #crear cursor
    c = conn.cursor()
    #insertar registro en tabla
    c.execute("INSERT INTO direcciones VALUES(:nombre,:apellido,:calle,:ciudad,:provincia,:codigo_postal)",
    {   "nombre":nombre.get(),
        "apellido":apellido.get(),
        "calle":calle.get(),
        "ciudad":ciudad.get(),
        "provincia":provincia.get(),
        "codigo_postal":codigo_postal.get()

    })
    #guardar cambios
    conn.commit()
    
    #cerrar conexion
    conn.close()

    nombre.delete(0,END)
    apellido.delete(0,END)
    calle.delete(0,END)
    ciudad.delete(0,END)
    provincia.delete(0,END)
    codigo_postal.delete(0,END)
    return

#funcion traer usuarios
def traer_usuarios():
    #crear o conectar una base de datos
    conn = sqlite3.connect('address_book.db')

    #crear cursor
    c = conn.cursor()
    c.execute("SELECT *, oid from direcciones")
    registros = c.fetchall()
    
    print_records = ""
    for registro in registros:
        for campo in registro:
            print_records += str(campo) + "\n" 
    label = Label(root,text=print_records)
    label.grid(row=60,column=0,columnspan=2)
    #guardar cambios
    conn.commit()
    
    #cerrar conexion
    conn.close()

    return 
# funcion eliminar usuario
def eliminar_registro():
    conn = sqlite3.connect('address_book.db')

    #crear cursor
    c = conn.cursor()
    c.execute("DELETE from direcciones WHERE oid =" + registro_a_eliminar.get())
   
    
    #guardar cambios
    conn.commit()
    
    #cerrar conexion
    conn.close()

def guardar_cambios():
    conn = sqlite3.connect('address_book.db')

    #crear cursor
    c = conn.cursor()

    id_a_editar = registro_a_eliminar.get()

    c.execute("""
        UPDATE direcciones SET 
        nombre = :nombre,
        apellido = :apellido,
        calle = :calle,
        ciudad = :ciudad,
        provincia = :provincia,
        codigo_postal = :codigo_postal
        
        WHERE oid = :oid""",
    {
        "nombre" : nombre_editor.get(),
        "apellido" : apellido_editor.get(),
        "calle" : calle_editor.get(),
        "ciudad" : ciudad_editor.get(),
        "provincia" : provincia_editor.get(),
        "codigo_postal" : codigo_postal_editor.get(),
        "oid": id_a_editar
    }
    )
    
    #guardar cambios
    conn.commit()
    
    #cerrar conexion
    conn.close()
    editor.destroy()

def editar():
    global editor
    editor=Tk()
    editor.title("Editar usuario")
    editor.geometry("400x200")

    conn = sqlite3.connect('address_book.db')

    #crear cursor
    c = conn.cursor()
    
    id_a_editar = registro_a_eliminar.get()
    c.execute("SELECT * from direcciones WHERE oid = " + id_a_editar)
    registros = c.fetchall()
    #crear variable globales 
    global nombre_editor
    global apellido_editor
    global calle_editor
    global ciudad_editor
    global provincia_editor
    global codigo_postal_editor

    #Crear formulario
    nombre_editor = Entry(editor,width=30)
    nombre_editor.grid(row = 0 , column=1,padx=20,pady=(10,0))

    apellido_editor = Entry(editor,width=30)
    apellido_editor.grid(row = 1 , column=1,padx=20)

    calle_editor = Entry(editor,width=30)
    calle_editor.grid(row = 2 , column=1,padx=20)

    ciudad_editor = Entry(editor,width=30)
    ciudad_editor.grid(row = 3 , column=1,padx=20)

    provincia_editor = Entry(editor,width=30)
    provincia_editor.grid(row = 4 , column=1,padx=20)

    codigo_postal_editor = Entry(editor,width=30)
    codigo_postal_editor.grid(row = 5 , column=1,padx=20)

    #Crear labels
    nombre_label_editor = Label(editor,text ="nombre")
    nombre_label_editor.grid(row=0,column=0,pady=(10,0))
    apellido_label_editor = Label(editor,text ="apellido")
    apellido_label_editor.grid(row=1,column=0)
    calle_label_editor = Label(editor,text ="calle")
    calle_label_editor.grid(row=2,column=0)
    ciudad_label_editor = Label(editor,text ="ciudad")
    ciudad_label_editor.grid(row=3,column=0)
    provincia_label_editor = Label(editor,text ="provincia")
    provincia_label_editor.grid(row=4,column=0)
    codigo_postal_label_editor = Label(editor,text ="codigo_postal")
    codigo_postal_label_editor.grid(row=5,column=0)
    
    #ciclar por elementos
    for registro in registros:
        nombre_editor.insert(0,registro[0])
        apellido_editor.insert(0,registro[1])
        calle_editor.insert(0,registro[2])
        ciudad_editor.insert(0,registro[3])
        provincia_editor.insert(0,registro[4])
        codigo_postal_editor.insert(0,registro[5])
    
    #crear boton para guardar datos
    boton_guardar_cambios=Button(editor,text="Guardar cambios",command=guardar_cambios)
    boton_guardar_cambios.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Crear formulario
nombre = Entry(root,width=30)
nombre.grid(row = 0 , column=1,padx=20,pady=(10,0))

apellido = Entry(root,width=30)
apellido.grid(row = 1 , column=1,padx=20)

calle = Entry(root,width=30)
calle.grid(row = 2 , column=1,padx=20)

ciudad = Entry(root,width=30)
ciudad.grid(row = 3 , column=1,padx=20)

provincia = Entry(root,width=30)
provincia.grid(row = 4 , column=1,padx=20)

codigo_postal = Entry(root,width=30)
codigo_postal.grid(row = 5 , column=1,padx=20)

registro_a_eliminar = Entry(root,width=30)
registro_a_eliminar.grid(row=9,column=1)

#Crear labels
nombre_label = Label(root,text ="nombre")
nombre_label.grid(row=0,column=0,pady=(10,0))
apellido_label = Label(root,text ="apellido")
apellido_label.grid(row=1,column=0)
calle_label = Label(root,text ="calle")
calle_label.grid(row=2,column=0)
ciudad_label = Label(root,text ="ciudad")
ciudad_label.grid(row=3,column=0)
provincia_label = Label(root,text ="provincia")
provincia_label.grid(row=4,column=0)
codigo_postal_label = Label(root,text ="codigo_postal")
codigo_postal_label.grid(row=5,column=0)
registro_a_eliminar_label=Label(root,text="seleccionar usuario")
registro_a_eliminar_label.grid(row=9,column=0,padx=20)

#crear boton para cargar datos
boton_crear_user=Button(root,text="Aceptar",command=submit)
boton_crear_user.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
boton_mostrar_registros=Button(root,text="mostrar registros",command=traer_usuarios)
boton_mostrar_registros.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
#crear boton eliminar registro
boton_eliminar_registro=Button(root,text="eliminar usuario",command=eliminar_registro)
boton_eliminar_registro.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
#crear boton editar registro
boton_editar_registro=Button(root,text="editar usuario",command=editar)
boton_editar_registro.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

mainloop()