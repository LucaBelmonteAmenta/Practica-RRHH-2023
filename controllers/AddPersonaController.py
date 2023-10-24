from tkinter import messagebox
from tkinter.constants import END
from models.Personas import Personas
from models.Competencias import Competencias
from models.RelacionesCompetenciaPersona import RelacionesCompetenciaPersona
from core.Controller import Controller


"""
    Responsible for AddView behavior.
"""
class AddPersonaController(Controller):


    personas = Personas()
    competencias = Competencias()

    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.addView = self.loadView("AddPersona")
        
        
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
 
 
    def btn_add_persona(self, fields):
        response = self.personas.addOne(fields)
        messagebox.showinfo("Registro Exitoso", "La persona fue registrada exitosamente.")
        self.addView.close()

    
    def btn_add_competencias(self, fields):
        persona = (Personas().getAllPersonas())[-1]["Id"]
        for field in fields:
            RelacionesCompetenciaPersona().addOne(persona,field["ID"])
        

    def selectListCompetencia(self):    
        SelectListsCompetencias = self.loadView("SelectListsCompetencias")


    def getAllCompetencias(self):
        return self.competencias.getAllCompetencias()
        
    
    def cargarCompetenciasElegidas(self, competencias):
        self.addView.cargarCompetenciasElegidas(competencias)




    def main(self):
        self.addView.main()