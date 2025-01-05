import tkinter as tk

#modulos restantes de tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *

class FormularioClientes:
 
 global base
 base =None

 global textBoxId
 textBoxId =None

 global textBoxNombres
 textBoxNombres =None

 global textBoxApellidos
 textBoxApellidos =None

 global combo
 combo =None

 global groupBox
 groupBox =None

 global tree
 tree =None 
     


def Formulario():
  global textBoxId
  global textBoxNombres
  global textBoxApellidos
  global combo
  global base
  global groupBox
  global tree

  try:
    base = Tk()
    base.geometry("1200x300")
    base.title("Formulario Python")

    groupBox = LabelFrame(base,text= "Datos del personal ", padx=5, pady=5)
    groupBox.grid(row=0,column=0,padx=10,pady=10)

    labelId=Label(groupBox,text="Id:",width=13, font=("arial",12)).grid(row=0,column=0)
    textBoxId= Entry(groupBox)
    textBoxId.grid(row=0,column=1)

    labelNombres=Label(groupBox,text="Nombres:",width=13, font=("arial",12)).grid(row=1 ,column=0)
    textBoxNombres= Entry(groupBox)
    textBoxNombres.grid(row=1,column=1)

    labelApellidos=Label(groupBox,text="Apellidos:",width=13, font=("arial",12)).grid(row=2,column=0)
    textBoxApellidos= Entry(groupBox)
    textBoxApellidos.grid(row=2,column=1)

    labelSexo=Label(groupBox,text="Sexo:",width=13, font=("arial",12)).grid(row=3,column=0)
    selectionSexo = tk.StringVar()
    combo= ttk.Combobox(groupBox, values= ["Masculino", "Femenino"],textvariable=selectionSexo)
    combo.grid(row=3,column=1)

    Button(groupBox, text="Guardar", width=10,command=guardarRegistros).grid(row=4,column=0) 
    Button(groupBox, text="Modificar", width=10).grid(row=4,column=1) 
    Button(groupBox, text="Eliminar", width=10).grid(row=4,column=2) 

    groupBox = LabelFrame(base, text= "Lista del personal", padx=5, pady=5,)
    groupBox.grid(row=0, column=1, padx=5, pady=5)

    #Crear un Treeview

    #configuarar columnas

    tree= ttk.Treeview(groupBox, columns=("Id", "Nombres", "Apellidos","Sexo"), show='headings',height=5,)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1 ",text="id")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2 ",text="Nombres")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3 ",text="Apellidos")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4 ",text="Sexo")

    tree.pack()







    base.mainloop()



  except ValueError as error:
           print("Error al mostarr la interfaz, error: {}".format(error)) 

def guardarRegistros():
    
    global textBoxNombres, textBoxApellidos, combo, groupBox

    try:
       #verificar si campos estan inicializados
       if textBoxNombres is None or textBoxApellidos is None or combo is None:
           print("Los campos no estan inicializados")
           return
       
       nombres = textBoxNombres.get()
       apellidos = textBoxApellidos.get()
       sexo = combo.get()

       CClientes.ingresarClientes(nombres,apellidos,sexo)
       messagebox.showinfo("Información", "Los datos fueron guardados")

       #Limpiamos los campos

       textBoxNombres.delete(0,END)
       textBoxApellidos.delete(0,END)

    except ValueError as error :
       print("Eror al ingresar los datos {}".format(error))   


Formulario()               