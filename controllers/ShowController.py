from core.Core import Core
from models.Personas import Personas
from models.Competencias import Competencias
from models.RelacionesCompetenciaPersona import RelacionesCompetenciaPersona
from core.Controller import Controller
from tkinter import messagebox
import datetime


"""
    Responsible for ShowView behavior.
"""
class ShowController(Controller):

    bdPersonas = Personas()
    bdCompetencias = Competencias()
    bdRelacionesCompetenciaPersona = RelacionesCompetenciaPersona()

    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
  
  
    def __init__(self):
        
        self.personas = self.bdPersonas.getAllPersonas()
        self.lista_filtrada = self.personas
        self.competencias_para_filtrar = []
        self.edades_para_filtrar = []

        
        self.showView = self.loadView("show")
        self.core = Core()


    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    def cargarCompetenciasElegidas(self, competencias):
        self.competencias_para_filtrar = competencias
        self.filtar()
        

    def selectListCompetencia(self):    
        SelectListsCompetencias = self.loadView("SelectListsCompetencias")

    def getAllCompetencias(self):
        return self.bdCompetencias.getAllCompetencias()
    
    def filtro_competencias(self):
        if self.competencias_para_filtrar:
            lista_personas = {}
            for competencia in self.competencias_para_filtrar:
                uniones = self.bdRelacionesCompetenciaPersona.getAllUnions_persona(competencia["ID"], False)
                for union in uniones:
                    if str(union["IdPersona"]) in lista_personas:
                        lista_personas[str(union["IdPersona"])] += 1
                    else:
                        lista_personas[str(union["IdPersona"])] = 1
            
            id_personas_filtradas = []

            for id_persona, numero_repeticiones in lista_personas.items():
                if numero_repeticiones == len(self.competencias_para_filtrar):
                    id_personas_filtradas.append(id_persona)

            nuevo_filtro = [persona for persona in self.lista_filtrada if str(persona["Id"]) in id_personas_filtradas]

            self.lista_filtrada = nuevo_filtro


    def cargarEdad(self, edad_min, edad_max):
        edad_min = int(edad_min)
        edad_max = int(edad_max)
        self.edades_para_filtrar = [min(edad_min, edad_max), max(edad_min, edad_max)]
        self.filtar()


    def filtro_edad(self):

        def Calcular_edad(born):
            #print(born)
            today = datetime.date.today()
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age

        if len(self.edades_para_filtrar) > 0:
            personas_filtradas = []
            for persona in self.lista_filtrada:
                fecha_nacimiento = datetime.datetime.strptime(persona["Fecha_nacimiento"], "%Y-%m-%d") 
                edad = Calcular_edad(fecha_nacimiento)
                print(self.edades_para_filtrar[0], edad ,self.edades_para_filtrar[1])
                if ((edad>=self.edades_para_filtrar[0]) and (edad<=self.edades_para_filtrar[1])):
                    personas_filtradas.append(persona)
            self.lista_filtrada = personas_filtradas


            

    def filtar(self):
        self.lista_filtrada = self.personas
        self.filtro_competencias()
        self.filtro_edad()
        self.showView.update()


    def main(self):
        self.showView.main()
