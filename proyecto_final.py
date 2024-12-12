import tkinter as tk
import random

def jugar(opcion_usuario):
    opciones = ['Piedra', 'Papel', 'Tijera']
    opcion_pc = random.choice(opciones)
    
    resultado = ''
    if opcion_usuario == opcion_pc:
        resultado = 'Empate'
    elif (opcion_usuario == 'Piedra' and opcion_pc == 'Tijera') or \
         (opcion_usuario == 'Papel' and opcion_pc == 'Piedra') or \
         (opcion_usuario == 'Tijera' and opcion_pc == 'Papel'):
        resultado = 'Ganaste'
    else:
        resultado = 'Perdiste'
    
    etiqueta_resultado.config(text=f'Tu elección: {opcion_usuario}\n'
                                   f'Elección de la máquina: {opcion_pc}\n'
                                   f'Resultado: {resultado}')

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

etiqueta_bienvenida = tk.Label(ventana, text="Bienvenidos a nuestro programa", font=("Arial", 14))
etiqueta_bienvenida.pack(pady=10)

boton_piedra = tk.Button(ventana, text="Piedra", command=lambda: jugar('Piedra'), width=10)
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="Papel", command=lambda: jugar('Papel'), width=10)
boton_papel.pack(pady=5)

boton_tijera = tk.Button(ventana, text="Tijera", command=lambda: jugar('Tijera'), width=10)
boton_tijera.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
