## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

import tkinter as tk
from tkinter import ttk

from ejercicio03 import ListaCiudades

class Ciudad:

    def __init__(self, ciudadesDesktop):
        self.ciudadesDesktop = ciudadesDesktop
        self.ciudadesDesktop.title("Ciudades")

    def ciudades(self):
        btnAdd = tk.Button(window, text="Agregar", command=self.nuevaCiudad)
        # btnAdd.grid(row=0, column=0)
        btnAdd.pack()

        btnDlt = tk.Button(window, text="Borrar", command=self.borrarCiudad)
        # btnDlt.grid(row=0, column=1)
        btnDlt.pack()

        btnMdf = tk.Button(window, text="Modificar", command=self.modificarCiudad)
        # btnMdf.grid(row=0, column=2)
        btnMdf.pack()

        self.trv = ListaCiudades(self.ciudadesDesktop)
        self.trv.pack()

    def nuevaCiudad(self):
        new = tk.Toplevel(window)

        frame = tk.LabelFrame(new, text="Ingresa nueva ciudad")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        lblCiudad = ttk.Label(frame, text="Ciudad: ")
        lblCiudad.grid(column=1, row=1)

        self.ciudad = tk.StringVar()
        self.txtCity = ttk.Entry(frame, width=15, textvariable=self.ciudad)
        self.txtCity.focus()
        self.txtCity.grid(column=1, row=1)

        lblPC = ttk.Label(frame, text="Código postal: ")
        lblPC.grid(column=0, row=2)

        self.pc = tk.StringVar()
        self.txtPC = ttk.Entry(frame, width=15, textvariable=self.pc)
        self.txtPC.grid(column=1, row=2)

        btnSave = ttk.Button(frame, text="Guardar ciudad", command=self.addCiudad)
        btnSave.grid(column=1, row=3, columnspan=2)

    def addCiudad(self):
        self.trv.insert("", "end", text=self.ciudad.get(), values=(self.pc.get()))
        self.txtCity.delete(0, tk.END)
        self.txtPC.delete(0, tk.END)

    def borrarCiudad(self):
        item = self.trv.selection()
        self.trv.delete(item)

    def modificarCiudad(self):
        try:
            self.trv.item(self.trv.selection())['text'][0]
        except IndexError:
            # mostrar error
            return

        new = tk.Toplevel(window)

        frame = tk.LabelFrame(new, text="Modifica una ciudad")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        curItem = self.trv.item(self.trv.selection())

        lblCity = ttk.Label(frame, text="Nombre anterior")
        lblCity.grid(column=0, row=1)

        lblCity = ttk.Label(frame, text=curItem["text"])
        lblCity.grid(column=1, row=1)

        lblCity = ttk.Label(frame, text="Nombre nuevo: ")
        lblCity.grid(column=0, row=2)

        self.ciudad = tk.StringVar()
        self.txtCity = ttk.Entry(frame, width=15, textvariable=self.ciudad)
        self.txtCity.focus()
        self.txtCity.grid(column=1, row=2)

        lblPC = ttk.Label(frame, text="Código postal anterior: ")
        lblPC.grid(column=0, row=3)

        lblPC = ttk.Label(frame, text=curItem["values"])
        lblPC.grid(column=1, row=3)

        lblPC = ttk.Label(frame, text="Codigo postal nuevo: ")
        lblPC.grid(column=0, row=4)

        self.pc = tk.StringVar()
        self.txtPC = ttk.Entry(frame, width=15, textvariable=self.pc)
        self.txtPC.grid(column=1, row=4)

        btnSave = ttk.Button(frame, text="Guardar ciudad", command=self.actualizaCiudad)
        btnSave.grid(column=1, row=5, columnspan=2)

    def actualizaCiudad(self):
        self.trv.item(self.trv.selection(), text=self.ciudad.get(), values=(self.pc.get()))
        self.txtCity.delete(0, tk.END)
        self.txtPC.delete(0, tk.END)


if __name__ == '__main__':
    window = tk.Tk()
    application = Ciudad(window)
    application.ciudades()
    window.mainloop()
