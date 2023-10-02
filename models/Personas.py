from Model import Model
import datetime

class Personas(Model):

    def __init__(self):

        estructuraTabla = [("Nombre",           "VARCHAR(20)",  False),
                           ("Apellido",         "VARCHAR(40)",  False),
                           ("Direccion",        "VARCHAR(50)",  False),
                           ("Fecha_nacimiento", "INT",          False),
                           ("Sexo",             "VARCHAR(10)",  False),
                           ("Work_For_Us",      "INT",          False),
                           ("Telefono",         "VARCHAR(10)",   False)
                           ]
        
        super().__init__(estructuraTabla)

    def addOne(self, 
               nombre, 
               apellido, 
               direccion, 
               fecha_nacimiento, 
               sexo, 
               work_For_Us,
               telefono):
        
        if work_For_Us is True:
            work_For_Us = 1
        else:
            work_For_Us = 0

        fecha_nacimiento = int(fecha_nacimiento.strftime("%d%m%Y"))

        dataNewPersona = {
            "Nombre" : nombre,
            "Apellido" : apellido,
            "Direccion": direccion,
            "Fecha_nacimiento": fecha_nacimiento,
            "Sexo": sexo,
            "Work_For_Us": work_For_Us,
            "Telefono": telefono,
        }

        self.IncertData(dataNewPersona)




if __name__ == '__main__':

    x = Personas()

    nombre = 'Lucas'
    apellido = 'Belmonte Amenta'
    direccion = 'the citadel, 17 city'
    fecha_nacimiento = datetime.date.today()
    sexo = 'Masculino'
    work_For_Us = True
    telefono = '0012341'

    x.addOne(nombre, 
            apellido, 
            direccion, 
            fecha_nacimiento, 
            sexo, 
            work_For_Us,
            telefono)
    
    print(x.GetAllData())
    print(x.DeleteData(1))
    print(x.GetAllData())
        

