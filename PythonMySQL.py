import tkinter as tk

#modulos restantes de tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox



class FormularioClientes:
     
 def Formulario():
  try:
    base = Tk()
    base.geometry("1200x300")
    base.title("Formulario Python")
    base.mainloop()



  except ValueError as error:
           print("Error al mostarr la interfaz, error: {}".format(error)) 

 Formulario()               