from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("mensajes")
root.geometry("500x500")

#crear o conectar una base de datos
conn = sqlite3.connect('address_book.db')

#crear cursor
c = conn.cursor()

#crear tabla
c.execute("""CREATE TABLE direcciones (
    nombre text,
    apellido text,
    calle text,
    ciudad text,
    provincia text,
    codigo_postal integer
)""")

conn.commit()

#cerrar conexion
conn.close()
mainloop()