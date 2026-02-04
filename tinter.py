#Importamos librerías
import tkinter as tk
from tkinter import ttk

#Definimos la ventana
ven1 = tk.Tk()
#Le damos un título a la ventana
ven1.title("Mi primera aplicación con Tkinter")
#Programamos dimensiones
ven1.geometry("1600x500")
# Iniciar el bucle principal de la aplicación
etiqueta = tk.Label(ven1,text="Lorem Ipsum", 
    font=("Arial", 14, "bold"), fg="black",padx=20, pady=10)
etiqueta.pack()
ven1.mainloop()