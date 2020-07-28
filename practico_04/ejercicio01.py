## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
 
import tkinter as tk

def calcular(operacion):
    if not tBV1.get() or not tBV2.get():
        print("Complete los campos")
    else:
        text = tBV1.get() + operacion + tBV2.get()
        print(eval(text))

window = tk.Tk()
window.title("Calculadora")

# Estiquetas
label1 = tk.Label(window, text="Primer operando")
label2 = tk.Label(window, text="Segundo operando")

# Estiquetas en pantalla
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)

# Entrada
tBV1 = tk.Entry(window, width=10)
tBV2 = tk.Entry(window, width=10)

# Entrada en pantalla
tBV1.grid(row=1, column=0, padx=5, pady=(5, 20))
tBV2.grid(row=1, column=1, padx=5, pady=(5, 20))

# Botones
btnSuma = tk.Button(window, text="+", heigh=1, command=lambda: calcular("+"))
btnResta = tk.Button(window, text="-", heigh=1, command=lambda: calcular("-"))
btnPor = tk.Button(window, text="x", heigh=1, command=lambda: calcular("*"))
btnDiv = tk.Button(window, text="%", heigh=1, command=lambda: calcular("/"))

# Botones en pantalla
btnSuma.grid(row=1, column=2, pady=(5, 20))
btnResta.grid(row=1, column=3, pady=(5, 20))
btnPor.grid(row=1, column=4, pady=(5, 20))
btnDiv.grid(row=1, column=5, pady=(5, 20), padx=(0, 20))

window.mainloop()
