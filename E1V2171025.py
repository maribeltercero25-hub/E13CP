#importar las bibliotecas
import tkinter as tk
#definir las funciones
def mostrar_ventana2():
    ventana1.withdraw() #oculte ventana 1
    ventana2.deiconfy() #muestre ventana 2

def regresar():
    ventana2.withdraw()#ocultar ventana 2
    ventana1.deiconfy()#mostrar ventana 1
#configurar la ventana 1
ventana1 = tk.Tk()
label1 = tk.Label(ventana1, text="ESTA ES MI VENTANA")
ventana1.geometry("600x400")
ventana1.config(bg="#F5F4ED")#agregamos color a la ventana

label1.pack()
btn1=tk.Button(ventana1,text="ir a ventana 2", command=mostrar_ventana2)
btn1.pack()

#creacion de la ventana 2
ventana2 = tk.Tk()
label2 = tk.Label(ventana2, text="ESTA ES MI VENTANA 2")
ventana2.geometry("600x400")
ventana2.config(bg="#E5F2D5")#agregar color a la ventana

label2.pack()
btn2=tk.Button(ventana2, text="ir a la ventana 1", command=regresar)
btn2.pack()

ventana2.withdraw()

ventana1.mainloop()