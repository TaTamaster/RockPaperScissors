import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
#from PIL import Image, ImageTk

# Función para determinar el ganador
def determinar_ganador(eleccion_usuario):
    opciones = ['piedra', 'papel', 'tijera']
    eleccion_computadora = random.choice(opciones)
    
    if eleccion_usuario == eleccion_computadora:
        resultado = 'Empate'
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
        resultado = '¡Ganaste!'
    else:
        resultado = 'Perdiste'
    
    messagebox.showinfo("Resultado", f"Elegiste {eleccion_usuario}, la computadora eligió {eleccion_computadora}. {resultado}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

# Cargar imágenes
imagen_piedra = ImageTk.PhotoImage(Image.open("piedra.png"))
imagen_papel = ImageTk.PhotoImage(Image.open("papel.png"))
imagen_tijera = ImageTk.PhotoImage(Image.open("tijera.png"))

# Crear botones
boton_piedra = tk.Button(ventana, image=imagen_piedra, command=lambda: determinar_ganador('piedra'))
boton_piedra.grid(row=0, column=0)

boton_papel = tk.Button(ventana, image=imagen_papel, command=lambda: determinar_ganador('papel'))
boton_papel.grid(row=0, column=1)

boton_tijera = tk.Button(ventana, image=imagen_tijera, command=lambda: determinar_ganador('tijera'))
boton_tijera.grid(row=0, column=2)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()