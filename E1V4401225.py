#modificamos la bienvenida 
#modificamos colores
#modificamos las medidas
 

import tkinter as tk
from tkinter import ttk

# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#CFE7DC"
COLOR_MENU = "#619E82"
COLOR_TEXTO = "#000000"
FUENTE_TITULO = ("Times", 24, "bold italic")
FUENTE_TEXTO = ("Times", 12)

# -------- VENTANA PRINCIPAL --------
root = tk.Tk()
root.title("Adicción a las redes sociales")
root.geometry("1500x800")
root.config(bg=COLOR_FONDO)
scrollbar= ttk.Scrollbar(orient=tk.VERTICAL)
scrollbar.set(0.2, 0.5)
scrollbar.place(x=50, y=50, height=200)


# -------- FRAME MENÚ LATERAL --------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# -------- FRAME CONTENIDO --------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- FUNCIÓN PARA CAMBIAR DE PÁGINA --------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# -------- PÁGINAS --------
def pagina_bienvenida():
    tk.Label(contenido_frame, 
             text="Bienvenido a nuestro Test ", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=30)
    
    tk.Label(contenido_frame, 
             text="Me alegra que estes aqui." \
             "Quiero que sepas que este es un espacio seguro donde nosotro podemos ayudarte a conocer si tienes alguna adiccion a las redes sociales," \
             " con una serie de preguntas reflexibas", 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, 
             text="Registro de Usuario", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=20)
    
    for campo in ["Nombre", "Edad", "Correo", "Número de Teléfono"]:
        tk.Label(contenido_frame, 
                 text=f"{campo}:", 
                 bg=COLOR_FONDO, 
                 font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)

def pagina_test():

    canvas = tk.Canvas(contenido_frame,bg=COLOR_FONDO, highlightthickness=0)
    scrollbar = ttk.Scrollbar(contenido_frame,orient="vertical",command=canvas.yview)
    scroll_frame = tk.Frame(canvas,bg=COLOR_FONDO)

    scroll_frame.bind(
        "<Configure>",
        lambda e:canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    ) 
    canvas.create_window((0,0),
    window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="y")
    tk.Label(contenido_frame, 
             text="Test de Adicción sobre las Redes Sociales", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame,
             text="¿Revisas tus redes sociales al despertar?",
             font=FUENTE_TEXTO,
            bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Sientes la necesidad de revisar tus notificaciones con frecuencia?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Te distraes de tus tareas diarias por revisar tus redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Utilizas redes sociales mientras comes o en reuniones?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Has intentado reducir el tiempo que pasas en redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)

    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Prefieres interactuar en línea en lugar de hacerlo en persona?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Publicas o compartes contenido en redes sociales con regularidad",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')

    tk.Label(contenido_frame,
             text="¿Te cuesta desconectarte de tus redes sociales antes de dormir?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Has perdido la noción del tiempo mientras navegas por redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Con que frecuencia revisas tus redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Te sientes ansioso o irritado si no puedes acceder a tus redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Utilizas redes sociales como forma de escapar de problemas?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Te preocupa no tener tu teléfono para ver tus redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Te sientes mal si no recibes atención en tus redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')
    tk.Label(contenido_frame,
             text="¿Sientes que tus relaciones personales se ven afectadas por el tiempo que pasas en redes sociales?",
             font=FUENTE_TEXTO,
             bg=COLOR_FONDO).pack(pady=10)
    chk1 = tk.Checkbutton(contenido_frame, 
                          text="Nunca")
    chk1.pack(anchor='center')

    chk2 = tk.Checkbutton(contenido_frame, text="A veces")
    chk2.pack(anchor='center')

    chk3 = tk.Checkbutton(contenido_frame, text="Siempre")
    chk3.pack(anchor='center')

    
tk.Label(contenido_frame, 
             text="Responde las siguientes preguntas de acuerdo a tu consumo de redes sociales.", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)

             
    
tk.Button(contenido_frame, text="Iniciar Test").pack(pady=20)

# -------- DICCIONARIO DE PÁGINAS --------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test
}

# -------- BOTONES DE MENÚ LATERAL --------
for nombre in paginas:
    ttk.Button(menu_frame, 
               text=nombre, 
               command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, 
           text="Salir", 
           command=root.quit).pack(side="bottom", pady=10)

# -------- MOSTRAR PÁGINA INICIAL --------
pagina_bienvenida()

# -------- BUCLE PRINCIPAL --------
root.mainloop()

