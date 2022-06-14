from ast import Str
from pydoc import text
from re import I
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title("Star Wars Info")
root.geometry("400x400")
#https://swapi.dev/api/planets
#https://swapi.dev/api/people
#https://swapi.dev/api/starships

def get_personajes():
    global personajes
    personajes=Toplevel()
    personajes.title("Personajes")
    personajes.geometry("400x300")
    request_api = requests.get("https://swapi.dev/api/people")
    try:
        api = json.loads(request_api.content)    
        for e,elemento in enumerate(api['results']):
            boton = Button(personajes,text = elemento["name"],borderwidth = 6,
                        width = 40, relief="ridge",command=lambda i = elemento["name"]:get_imagen_personaje(i))
            boton.grid(row=e,column=0)
    except Exception as e:
        api = "Error"
    boton = Button(personajes,text="Volver",command=personajes.withdraw)
    boton.grid(row=1,column=2)

def get_vehiculos():
    global vehiculos
    vehiculos=Toplevel()
    vehiculos.title("Vehiculos")
    vehiculos.geometry("400x300")
    request_api = requests.get("https://swapi.dev/api/starships")
    try:
        api = json.loads(request_api.content)       
        for e, elemento in enumerate(api['results']): 
            boton = Button(vehiculos,text = elemento["name"],borderwidth = 6,
                         width = 40, relief="ridge",command=lambda i=elemento["name"]: get_imagen_vehiculos(i))
            boton.grid(row=e,column=0)

    except Exception as e:
        api = "Error"
    boton = Button(vehiculos,text="Volver",command=vehiculos.withdraw)
    boton.grid(row=1,column=3)

def get_imagen_personaje(nombre):
    global label
    global imagen_personaje
    global frame
    frame =  LabelFrame(personajes)
    personajes_dict = {
                'Luke Skywalker' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/luke_sky.jpg',
                'C-3PO' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/c3po.jpg',
                'R2-D2' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/r2d2.webp',
                'Darth Vader' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/darth_vader.webp',
                'Leia Organa' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/leia.webp',
                'Owen Lars' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/owen_lars.jpg',
                'Beru Whitesun lars' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/beru_whitesun.webp',
                'R5-D4' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/R5d4.webp',
                'Biggs Darklighter': r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/biggs_darklighter.jpg',
                "Obi-Wan Kenobi": r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/obi_wan.jpeg'
                }
    frame.destroy()
    frame = LabelFrame(personajes,padx=20,pady=20)
    frame.grid(row=0,column=2,padx=10,pady=10)
    frame.configure(text=nombre)
    imagen_personaje = ImageTk.PhotoImage(Image.open(personajes_dict[nombre]).resize((500,400),Image.ANTIALIAS))
    label = Label(frame,image=imagen_personaje)
    label.pack()

def get_imagen_vehiculos(nombre):
    global label
    global imagen_vehiculos
    global frame
    frame =  LabelFrame(vehiculos)
    vehiculos_dict = {
                'CR90 corvette' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/cr90_corvette.jfif',
                'Star Destroyer' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/star_destroyer.webp',
                'Sentinel-class landing craft' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/Sentinel_class_landing.webp',
                'Death Star' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/Death-Star-I.jpeg',
                'Millennium Falcon' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/Millennium_Falcon.webp',
                'Y-wing' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/Y-Wing.jpeg',
                'X-wing' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/xwing.jfif',
                'TIE Advanced x1' : r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/TIE_Avanzado_X1.webp',
                'Executor': r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/Executor_BF2.webp',
                "Rebel transport": r'C:/Users/ezequiel.chiacchio/Eze/pthon/tkinter/imagenes/swapi_app/rebel_transport.webp'
                }
    frame.destroy()
    frame = LabelFrame(vehiculos,padx=20,pady=20)
    frame.grid(row=0,column=2,padx=10,pady=10)
    frame.configure(text=nombre)
    imagen_vehiculos = ImageTk.PhotoImage(Image.open(vehiculos_dict[nombre]).resize((400,300),Image.ANTIALIAS))
    label = Label(frame,image=imagen_vehiculos)
    label.pack()



boton = Button(root,text="Mostrar personajes",command=get_personajes).pack()
boton = Button(root,text="Mostrar vehiculos",command=get_vehiculos).pack()

global img
img = ImageTk.PhotoImage(Image.open("imagenes/swapi_app/Star_Wars_Logo.svg.png").resize((400,300),Image.ANTIALIAS))
nueva_imagen = Label(image = img,width=400,height=300)
nueva_imagen.pack()
mainloop()