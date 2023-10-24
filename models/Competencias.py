from models.Model import Model
import datetime

class Competencias(Model):

    estructuraTabla = [("Descripcion",  "TEXT",  False),
                       ("Diciplina",  "VARCHAR(50)",  False)]

    def __init__(self):
        super().__init__(self.estructuraTabla, True)

    def addOne(self, descripcion, diciplina):
        dataNewCompetencia = { "Descripcion" : descripcion, "Diciplina" : diciplina }
        self.IncertData(dataNewCompetencia)

    def getAllCompetencias(self):
        competencias = self.GetAllData()

        lista_competencias = [] 
        for competencia in competencias:
            diccionario = {}

            diccionario["ID"] = competencia[0]
            diccionario["Descripcion"] = competencia[1]
            diccionario["Diciplina"] = competencia[2]

            lista_competencias.append(diccionario)

        return lista_competencias



if __name__ == '__main__':

    x = Competencias()

    #x.addOne("caca", "medicina")

    print(x.GetAllData())
    #print(x.DeleteData(8))
        

