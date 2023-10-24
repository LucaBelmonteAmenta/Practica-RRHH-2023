import sqlite3
import traceback
import sys

path_data_base = "/home/tecnicus/Documentos/Repositorios/Practica-RRHH-2023/db/"
nombre_base_datos = "InventarioRecursosHumanos.db"

class Model():

    #-----------------------------------------------------------------------
    #       estructuraTabla
    #       |   estructuraTabla[?][0] -> nombre del campo
    #       |   estructuraTabla[?][1] -> tipo de dato del campo
    #       |   estructuraTabla[?][2] -> puede ser null?
    #
    #       estructuraTabla[?] == item
    #----------------------------------------------------------------------- 
    
    def __init__(self, estructuraTabla, automaticSimpleId):
        
        conexion = sqlite3.connect(path_data_base+nombre_base_datos)

        if automaticSimpleId == True:
            campos_tabla = "Id INTEGER PRIMARY KEY AUTOINCREMENT, "
        else:
            campos_tabla = ""
        
        for item in estructuraTabla:
            if item[2] == False:
                null = "NOT NULL"
            else:
                null = ""
            campos_tabla += f"{item[0]} {item[1]} {null}, "
        
        campos_tabla = campos_tabla[:-2]
        nombre_clase = type(self).__name__
        comandoSQL = f"CREATE TABLE IF NOT EXISTS {nombre_clase} ({campos_tabla});"

        cursor = conexion.cursor()
        cursor.execute(comandoSQL)
        conexion.commit()
        conexion.close()


    def RunCommand(self, comandoSQL, datos_insercion = None):

        try:
            conexion = sqlite3.connect(path_data_base+nombre_base_datos)

            cursor = conexion.cursor()

            if datos_insercion is None:
                cursor.execute(comandoSQL)
            else:
                cursor.execute(comandoSQL, datos_insercion)

            if "SELECT" in comandoSQL:
                dataReturn = cursor.fetchall()
            else:
                conexion.commit()

            conexion.close()

            if "SELECT" in comandoSQL:
                return dataReturn
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        
    #-----------------------------------------------------------------------
    #       Data
    #       |   Clave -> nombre del campo
    #       |   Valor -> contenido del campo
    #-----------------------------------------------------------------------   

    def IncertData(self, data):
        
        campos = ""
        valores = ""

        for clave, valor in data.items():
            campos += f"{clave}, "
            valores += f"?, "

        campos = campos[:-2]
        valores = valores[:-2]

        nombre_clase = type(self).__name__
        comandoSQL = f"INSERT INTO {nombre_clase} ({campos}) VALUES({valores}); " 

        #print(comandoSQL)

        self.RunCommand(comandoSQL, tuple(data.values()))


    
    def GetAllData(self):
        nombre_clase = type(self).__name__
        comandoSQL = f"SELECT * FROM {nombre_clase}"
        dataReturn = self.RunCommand(comandoSQL)
        return dataReturn
    

    def getData(self, data): 
        condiciones = ""
        for clave, valor in data.items():
            condiciones += f"{clave} == {valor} AND"
        condiciones = condiciones[:-3]

        nombre_clase = type(self).__name__
        comandoSQL = f"SELECT * FROM {nombre_clase} WHERE {condiciones};"
        dataReturn = self.RunCommand(comandoSQL)
        return dataReturn


    def UpdateData(self, data, id):
        cambios = ""

        for clave, valor in data.items():
            cambios += f"{clave} = {valor}, "
        cambios = cambios[:-2]

        nombre_clase = type(self).__name__
        comandoSQL = f"UPDATE {nombre_clase} SET {cambios} WHERE Id = {id}; " 

        self.RunCommand(comandoSQL)


    def DeleteData(self, id):
        nombre_clase = type(self).__name__
        comandoSQL = f"DELETE FROM {nombre_clase} WHERE Id = {id}; " 
        self.RunCommand(comandoSQL)
