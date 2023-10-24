# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core


"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """
    def btnClicked(self, caption):
        if caption == "Busqueda de Personal":
            c = Core.openController("Show")
            c.main()
        elif caption == "Resgistrar nueva persona":
            c = Core.openController("AddPersona")
            c.main()
        elif caption == "Administrador de Competencias":
            c = Core.openController("ShowCompetencias")
            c.main()
            
    """
        @Override
    """
    def main(self):
        self.homeView.main()