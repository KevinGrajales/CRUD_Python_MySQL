#pip install mysql-connector-phyton
import mysql.connector

class CConexion:

   def conexionBaseDeDatos():
    try:
        conexion = mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='clientesdb',port='3306')

        print("Conexion Correcta")

        return conexion

    except mysql.connector.Error as error:
        print("Error al conectarte a la base de datos {}".format(error))

        return conexion
    
   conexionBaseDeDatos()
    