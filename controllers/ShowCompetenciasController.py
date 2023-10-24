from tkinter import messagebox
from tkinter.constants import END
from models.Competencias import Competencias
from core.Controller import Controller


class ShowCompetenciasController(Controller):

    competencias = Competencias()

    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.addView = self.loadView("ShowCompetencias")
        
        
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    def addCompetencia(self):
        AddCompetenciaView = self.loadView("AddCompetencia")

    def btn_add(self, competencia, diciplina):
        response = self.competencias.addOne(competencia, diciplina)
        messagebox.showinfo("Registro Exitoso", "La competencia fue registrada exitosamente.")
        self.addView.close()
   
    """
        @Override
    """
    def main(self):
        self.addView.main()