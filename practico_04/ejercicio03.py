## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

import tkinter as tk
from tkinter import ttk

def ListaCiudades(window):
    trv = ttk.Treeview(window)
    trv["columns"] = ("one")
    trv.column("#0", width=150, minwidth=270, stretch=tk.NO)
    trv.column("one", width=150, minwidth=150, stretch=tk.NO)
    trv.heading("#0", text="Ciudades", anchor=tk.W)
    trv.heading("one", text="Código Postal", anchor=tk.W)
    trv.insert("", "end", text="Buenos Aires", values=("1675"))
    trv.insert("", "end", text="Rosario", values=("2000"))
    trv.insert("", "end", text="Pergamino", values=("2700"))
    trv.insert("", "end", text="Colón", values=("2720"))
    trv.insert("", "end", text="Córdoba", values=("5000"))

    return trv

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Vista de árbol en Tkinter")
    ListaCiudades(window).pack()
    window.mainloop()
