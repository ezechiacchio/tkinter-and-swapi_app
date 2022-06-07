from ast import Str
from pydoc import text
from re import I
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
import json

from Boton_custom import Boton_Custom

root=Tk()
root.title("Star Wars Info")
root.geometry("400x400")
#https://swapi.dev/api/planets
#https://swapi.dev/api/people
#https://swapi.dev/api/starships
def get_planetas():
    global planetas
    planetas=Tk()
    planetas.title("Planetas")
    planetas.geometry("400x300")
    request_api = requests.get("https://swapi.dev/api/planets")
    try:
        api = json.loads(request_api.content)    
        for elemento in api['results']:
            label = Label(planetas,text = elemento["name"],borderwidth = 6,
                        width = 40,
                        relief="ridge")
            label.pack()
    except Exception as e:
        api = "Error"

def get_personajes():
    global personajes
    personajes=Tk()
    personajes.title("Personajes")
    personajes.geometry("400x300")
    request_api = requests.get("https://swapi.dev/api/people")
    try:
        api = json.loads(request_api.content)    
        for elemento in api['results']:
            label = Label(personajes,text = elemento["name"],borderwidth = 6,
                        width = 40,
                        relief="ridge")
            label.pack()
    except Exception as e:
        api = "Error"

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
                         width = 40, relief="ridge",command=lambda i=elemento["name"]: get_imagen(i))
            boton.grid(row=e,column=0)
        label = Label(vehiculos,text="    ")
        label.grid(row=0,column=1)

    except Exception as e:
        api = "Error"

def get_imagen(nombre):
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



boton = Button(root,text="Mostrar planetas",command=get_planetas).pack()
boton = Button(root,text="Mostrar personajes",command=get_personajes).pack()
boton = Button(root,text="Mostrar vehiculos",command=get_vehiculos).pack()

global img
img = ImageTk.PhotoImage(Image.open("imagenes/swapi_app/Star_Wars_Logo.svg.png").resize((400,300),Image.ANTIALIAS))
nueva_imagen = Label(image = img,width=400,height=300)
nueva_imagen.pack()
mainloop()