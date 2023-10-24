from models.Model import Model
import datetime

class RelacionesCompetenciaPersona(Model):

    estructuraTabla = [("IdPersona",  "INTEGER",  False),
                       ("IdCompetencia",  "INTEGER",  False)]

    def __init__(self):
        super().__init__(self.estructuraTabla, True)


    def addOne(self, persona, competencia):
        dataNewUnion = { "IdPersona" : persona, "IdCompetencia" : competencia }
        #print(dataNewUnion)
        self.IncertData(dataNewUnion)


    def getAllUnions(self):

        uniones = self.GetAllData()
        lista_uniones = [] 

        for union in uniones:
            diccionario = {}

            diccionario["ID"] = union[0]
            diccionario["IdPersona"] = union[1]
            diccionario["IdCompetencia"] = union[2]

            lista_uniones.append(diccionario)

        return lista_uniones

    
    def getAllUnions_persona(self, data, por_persona):

        uniones = self.GetAllData()
        lista_uniones = [] 

        if (por_persona == True):
            condicion = 1
        else:
            condicion = 2

        for union in uniones:
            if (union[condicion] == data):
                diccionario = {}
                
                diccionario["ID"] = union[0]
                diccionario["IdPersona"] = union[1]
                diccionario["IdCompetencia"] = union[2]

                lista_uniones.append(diccionario)

        return lista_uniones
    


if __name__ == '__main__':
    pass