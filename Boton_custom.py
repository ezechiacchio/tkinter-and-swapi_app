from tkinter import Button


class Boton_Custom:
    def __init__(self , id_boton ,pagina, texto, borde, width, relief, comando) -> None:
        self.id = id_boton
        self.boton = Button(pagina,text = texto,borderwidth=borde,width=width,relief=relief,command = comando)
    def get_boton(self):
        return self.boton