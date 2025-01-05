from Conexion import *

class CClientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
         cone = CConexion.conexionBaseDeDatos()
         cursor = cone.cursor()
         sql = "insert into usuarios values(null, %s, %s, %s);"
         # variable valores debe ser una tupla (listas inmutables)
         # como valor minimo es: (valor,) la , hace que sea una tupla
         valores = (nombres,apellidos,sexo)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro ingresado")
         cone.close() 

        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))    