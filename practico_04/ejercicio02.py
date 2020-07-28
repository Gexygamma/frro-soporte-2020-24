## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

import tkinter as tk

window = tk.Tk()
window.title("Calculadora")

# Display
tBdisplay = tk.Entry(window, width=20, font=("Arial 16"))
tBdisplay.grid(column=0, row=1, columnspan=4, pady=20, padx=5)

i = 0

# Funciones
def click_button(valor):
    global i
    tBdisplay.insert(i, valor)
    i += 1

def borrar():
    tBdisplay.delete(0, tk.END)
    i = 0

def operacion():
    if len(tBdisplay.get()):
        resultado = eval(tBdisplay.get())
        tBdisplay.delete(0, tk.END)
        tBdisplay.insert(0, resultado)
        i = 0

# Botones
btn1 = tk.Button(window, text='1', width=5, heigh=2, command=lambda: click_button('1'))
btn2 = tk.Button(window, text='2', width=5, heigh=2, command=lambda: click_button('2'))
btn3 = tk.Button(window, text='3', width=5, heigh=2, command=lambda: click_button('3'))
btn4 = tk.Button(window, text='4', width=5, heigh=2, command=lambda: click_button('4'))
btn5 = tk.Button(window, text='5', width=5, heigh=2, command=lambda: click_button('5'))
btn6 = tk.Button(window, text='6', width=5, heigh=2, command=lambda: click_button('6'))
btn7 = tk.Button(window, text='7', width=5, heigh=2, command=lambda: click_button('7'))
btn8 = tk.Button(window, text='8', width=5, heigh=2, command=lambda: click_button('8'))
btn9 = tk.Button(window, text='9', width=5, heigh=2, command=lambda: click_button('9'))
btn0 = tk.Button(window, text='0', width=5, heigh=2, command=lambda: click_button('0'))

btn_sum = tk.Button(window, text='+', width=5, heigh=2, command=lambda: click_button('+'))
btn_res = tk.Button(window, text='-', width=5, heigh=2, command=lambda: click_button('-'))
btn_div = tk.Button(window, text='/', width=5, heigh=2, command=lambda: click_button('/'))
btn_mul = tk.Button(window, text='x', width=5, heigh=2, command=lambda: click_button('*'))
btn_paren1 = tk.Button(window, text='(', width=5, heigh=2, command=lambda: click_button('('))
btn_paren2 = tk.Button(window, text=')', width=5, heigh=2, command=lambda: click_button(')'))
btn_punto = tk.Button(window, text='.', width=5, heigh=2, command=lambda: click_button('.'))
btn_ac = tk.Button(window, text='AC', width=5, heigh=2, command=lambda: borrar())
btn_igual = tk.Button(window, text='=', width=13, heigh=2, command=lambda: operacion())

# Disposicion
btn_ac.grid(row=3, column=0, padx=5, pady=(0, 5))
btn_paren1.grid(row=3, column=1, padx=6, pady=(0, 5))
btn_paren2.grid(row=3, column=2, padx=6, pady=(0, 5))
btn_div.grid(row=3, column=3, padx=6, pady=(0, 5))

btn7.grid(row=4, column=0, padx=6, pady=5)
btn8.grid(row=4, column=1, padx=6, pady=5)
btn9.grid(row=4, column=2, padx=6, pady=5)
btn_mul.grid(row=4, column=3, padx=6, pady=5)

btn4.grid(row=5, column=0, padx=6, pady=5)
btn5.grid(row=5, column=1, padx=6, pady=5)
btn6.grid(row=5, column=2, padx=6, pady=5)
btn_res.grid(row=5, column=3, padx=6, pady=5)

btn1.grid(row=6, column=0, padx=6, pady=5)
btn2.grid(row=6, column=1, padx=6, pady=5)
btn3.grid(row=6, column=2, padx=6, pady=5)
btn_sum.grid(row=6, column=3, padx=6, pady=5)

btn0.grid(row=7, column=0, padx=6, pady=(5, 20))
btn_punto.grid(row=7, column=1, padx=6, pady=(5, 20))
btn_igual.grid(row=7, column=2, padx=6, pady=(5, 20), columnspan=2)

window.mainloop()
