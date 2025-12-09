import tkinter as tk
from tkinter import ttk

#...........CONFIGURACION DE COLORES Y FUENTE............
COLOR_FONDO = "#F5F4ED"
COLOR_MENU = "#E5F2D5"
COLOR_TEXTO = "#FAEFDE"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("arial",12)

#...........VENTANA PRINCIPAL..............
root = tk.Tk()
root.title("Bienestar total")
root.geometry("950x600")
root.config(bg=COLOR_FONDO)

#...........FRAME MENU LATERAL............
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

#...........FRAME CONTENIDO..................
contenido_frame =tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

#...........FUNCION PARA CAMBIAR DE PAGINA...........
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

#............PAGINAS...........
def pagina_bienvenida():
    tk.Label(contenido_frame, text="bienvenido abienestar total", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="un espacio de apoyo e informacion para tu salud.", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="registro de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)

    #CAMPO NOMBRE
    tk.Label(contenido_frame, text="Nombre", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)

    #CAMPO EDAD
    tk.Label(contenido_frame, text="Edad", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)

    #CAMPO CORREO
    tk.Label(contenido_frame, text="Correo", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width="Correo", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)

    #CAMPO SEMESTRE
    tk.Label(contenido_frame, text="Semestre", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width="Semestre", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)

def pagina_test():
    tk.Label(contenido_frame, text="TEST DE ADICCIONES", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="RESPONDE LAS SIGUIENTES PREGUMTAS PARA DETECTAR SI ERES UN ADICTO A LOS VIDEOJUEGOS", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="INICIAR TEST").pack(pady=20)

#..............DICCIONARIO DE PAGINAS............
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}
#...........BOTONES DE MENU LATERAL.............
for nombre in paginas:
    ttk.Button(menu_frame, text="salir", command=root.quit).pack(side="bottom", pady=10)

#...........MOSTRAR PAGINA INICIAL............
pagina_bienvenida()

root.mainloop()
